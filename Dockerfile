# Usa la imagen oficial de Odoo
FROM odoo:17

# Instala las dependencias necesarias (opcional)
USER root
RUN apt-get update && apt-get install -y \
    python3-pip \
    && rm -rf /var/lib/apt/lists/*

# Copia los addons adicionales
COPY ./addons /mnt/extra-addons

# Ajusta permisos para los archivos copiados
RUN chown -R odoo:odoo /mnt/extra-addons

# Copia archivos de configuración
COPY ./config /etc/odoo

# Cambia al usuario odoo
USER odoo
