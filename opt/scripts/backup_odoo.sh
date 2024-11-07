#!/bin/bash

# Configura las variables
ODOO_DB_NAME=peluqueria-canina
ODOO_DB_USER=postgres
ODOO_DB_PASSWORD=Carpetas22
ODOO_DB_HOST=http://18.231.162.172/ # O la IP del contenedor o servicio DB si es remoto
ODOO_DB_PORT=5432
S3_BUCKET_NAME=peluqueriacaninachajari
DATE=$(date +\%F_\%T) # Formato de fecha para el archivo de backup
BACKUP_FILE="/tmp/odoo_backup_${DATE}.sql"

# Realiza el volcado de la base de datos
PGPASSWORD=$ODOO_DB_PASSWORD pg_dump -h $ODOO_DB_HOST -U $ODOO_DB_USER -p $ODOO_DB_PORT $ODOO_DB_NAME > $BACKUP_FILE

# Comprime el archivo de respaldo (opcional)
gzip $BACKUP_FILE

# Subir el archivo comprimido a S3
aws s3 cp ${BACKUP_FILE}.gz s3://$S3_BUCKET_NAME/odoo_backups/

# Elimina el archivo local después de subirlo (opcional)
rm -f ${BACKUP_FILE}.gz

echo "Backup completado y enviado a S3."
