from flask import Blueprint, render_template, redirect, url_for, flash, request, current_app
from flask_login import login_required, current_user
from app.records.models import Record
from app import srp

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
            # Obtener URL de la portada (puede ser None si no se encontró)
            cover_url = request.form.get('cover_url')
            
            record = Record(
                title=request.form.get('title'),
                artist=request.form.get('artist'),
                year=int(request.form.get('year')),
                genre=request.form.get('genre'),
                condition=request.form.get('condition'),
                user_email=current_user.email,
                cover_url=cover_url  # Añadimos el nuevo campo
            )
            
            srp.save(record)
            flash('Disco añadido correctamente!', 'success')
            return redirect(url_for('records.list'))
            
        except ValueError as e:
            flash('El año debe ser un número válido', 'error')
            current_app.logger.error(f"ValueError in add: {str(e)}")
        except Exception as e:
            flash('Error al añadir el disco', 'error')
            current_app.logger.error(f"Add record error: {str(e)}")
    
    return render_template('records/add.html')