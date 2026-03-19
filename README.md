# template-vars

Plantilla minima de SPAI para probar variables de entrada en templates.

## Estructura

- `spai.config.yaml`: configuracion del proyecto SPAI.
- `spai.vars.json`: variables globales por defecto.
- `scripts/test/main.py`: script de ejemplo que lee variables.
- `scripts/test/requirements.txt`: dependencias del servicio.

## Variables incluidas

- `MESSAGE` (texto)
- `MAX_ITEMS` (numero)
- `some_data` (lista de numeros)

## Uso local

```bash
spai install
spai run
```

## Sobrescribir variables desde CLI

```bash
spai run -v MESSAGE='hola desde cli' -v MAX_ITEMS=25
spai deploy -t template-vars -v MESSAGE='produccion' -v MAX_ITEMS=50
```

## Notas

- `MAX_ITEMS` debe ser numerico (`int` o `float`).
- `MESSAGE` debe ser texto (`string`).
