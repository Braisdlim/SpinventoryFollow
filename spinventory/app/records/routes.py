from flask import Blueprint, render_template, redirect, url_for, flash, request, current_app, jsonify
from flask_login import login_required, current_user
from app.records.models import Record
from app import srp
from app.services.discogs_service import DiscogsService  # Nueva importación

# Definición del Blueprint
records_bp = Blueprint('records', __name__)

@records_bp.route('/list')
@login_required
def list():
    try:
        records = []
        for record in srp.load_all(Record):
            if record.user_email == current_user.email:
                records.append(record)
        return render_template('records/list.html', records=records)
    except Exception as e:
        flash('Error al cargar los discos', 'error')
        current_app.logger.error(f"Error en list: {str(e)}")
        return redirect(url_for('auth.login'))

@records_bp.route('/add', methods=['GET', 'POST'])
@login_required
def add():
    if request.method == 'POST':
        try:
            # Obtener datos del formulario
            title = request.form['title']
            artist = request.form['artist']
            year = int(request.form['year'])
            genre = request.form['genre']
            condition = request.form['condition']
            
            # Manejo de la portada (prioriza manual > automática > placeholder)
            cover_url = request.form.get('cover_url')
            if not cover_url:  # Búsqueda automática solo si no hay URL manual
                cover_url = DiscogsService.search_cover(artist, title)
            
            # Crear y guardar el registro
            record = Record(
                title=title,
                artist=artist,
                year=year,
                genre=genre,
                condition=condition,
                user_email=current_user.email,
                cover_url=cover_url  # Esto nunca será None
            )
            srp.save(record)
            
            flash('Disco añadido correctamente!', 'success')
            return redirect(url_for('records.list'))
            
        except Exception as e:
            current_app.logger.error(f"Error al añadir disco: {str(e)}")
            flash('Error al guardar el disco', 'error')
    
    return render_template('records/add.html')

@records_bp.route('/search-cover')
@login_required
def search_cover():
    """Endpoint para búsqueda AJAX de portadas"""
    try:
        artist = request.args.get('artist')
        title = request.args.get('title')
        
        if not artist or not title:
            return jsonify({"error": "Artista y título requeridos"}), 400
            
        cover_url = DiscogsService.search_cover(artist, title)
        
        if cover_url:
            return jsonify({"cover_url": cover_url})
        else:
            return jsonify({"error": "No se encontró portada"}), 404
            
    except Exception as e:
        current_app.logger.error(f"Error en búsqueda de portada: {str(e)}")
        return jsonify({"error": "Error en el servidor"}), 500