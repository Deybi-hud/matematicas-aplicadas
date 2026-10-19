# Matemáticas Aplicadas (MAT2121)

Repositorio de actividades, talleres y evaluaciones de **Matemáticas Aplicadas**, desarrollado principalmente en **Python** y **Jupyter Notebook**.

Este espacio documenta ejercicios de análisis matemático, modelado funcional, optimización y visualización gráfica aplicados a problemas del mundo real (redes, análisis de costos, consumo energético, cifrado de datos y climatología).

---

## Estructura del Repositorio

```text
matematicas-aplicadas/
├── .gitignore                          # Exclusión de checkpoints y archivos temporales
├── requirements.txt                    # Dependencias del proyecto
├── README.md                           # Documentación principal
└── Actividades/
    ├── Guias/                          # Guías de ejercicios y práctica de funciones
    │   ├── G1_Funciones.ipynb          # Guía 1: Modelado funcional básico
    │   └── G2_Funciones.ipynb          # Guía 2: Funciones avanzadas y análisis de eficiencia
    ├── Talleres/                       # Talleres evaluados y de preparación
    │   ├── Preparacion_Taller_1.ipynb  # Práctica: Consumo eléctrico y gestión de residuos
    │   ├── T1_MAT2121_FB.ipynb         # Taller 1 (Fila B): Modelado de lluvias torrenciales
    │   └── T2_MAT2121_FA.ipynb         # Taller 2 (Fila A): Batalla de cifrado (lineal vs polinomial)
    └── Evaluaciones/                   # Ensayos de pruebas, cuestionarios y scripts
        ├── Cuestionario_EA1.ipynb      # Cuestionario: Evaluación Auténtica 1
        ├── Ensayo_Prueba_1_MAT2121.ipynb # Ensayo y preparación para Prueba 1
        └── scripts/
            ├── Pregunta_12.py          # Script: Comparación de costos en sitios web
            └── Solucion_Prueba.py      # Script: Resolución numérica y gráfica con fsolve
```

---

## Contenido Detallado

### 1. Guías de Trabajo (`Actividades/Guias/`)
- **[G1_Funciones.ipynb](Actividades/Guias/G1_Funciones.ipynb)**: Modelado de funciones para transmisión de datos, costos de producción y variación temporal.
- **[G2_Funciones.ipynb](Actividades/Guias/G2_Funciones.ipynb)**: Evaluación de eficiencia de algoritmos, funciones cuadráticas y no lineales.

### 2. Talleres (`Actividades/Talleres/`)
- **[Preparacion_Taller_1.ipynb](Actividades/Talleres/Preparacion_Taller_1.ipynb)**: Resolución de problemas de consumo eléctrico durante olas de calor y gestión de residuos urbanos.
- **[T1_MAT2121_FB.ipynb](Actividades/Talleres/T1_MAT2121_FB.ipynb)**: Taller 1 - Modelado de caudales y prevención de inundaciones.
- **[T2_MAT2121_FA.ipynb](Actividades/Talleres/T2_MAT2121_FA.ipynb)**: Taller 2 - Comparativa de algoritmos de cifrado lineal vs polinomial.

### 3. Evaluaciones y Ensayos (`Actividades/Evaluaciones/`)
- **[Cuestionario_EA1.ipynb](Actividades/Evaluaciones/Cuestionario_EA1.ipynb)**: Preguntas de contexto y dominio para la evaluación auténtica 1.
- **[Ensayo_Prueba_1_MAT2121.ipynb](Actividades/Evaluaciones/Ensayo_Prueba_1_MAT2121.ipynb)**: Simulacro integral de Prueba 1 con problemas contextualizados (microservicios, transporte privado, etc.).
- **[scripts/](Actividades/Evaluaciones/scripts/)**:
  - `Pregunta_12.py`: Análisis de punto de equilibrio y conveniencia de costos con Matplotlib.
  - `Solucion_Prueba.py`: Resolución de intersecciones y ecuaciones con `scipy.optimize.fsolve`.

---

## Tecnologías y Librerías

- **[Python 3.10+](https://www.python.org/)**
- **[NumPy](https://numpy.org/)**: Operaciones matriciales y cálculo numérico.
- **[SciPy](https://scipy.org/)**: Optimización y resolución de ecuaciones no lineales (`fsolve`).
- **[Matplotlib](https://matplotlib.org/)**: Gráficos 2D, curvas de nivel y visualizaciones comparativas.
- **[Jupyter Notebook](https://jupyter.org/)**: Cuadernos interactivos para experimentación y documentación paso a paso.

---

## Instalación y Uso

### 1. Clonar el repositorio
```bash
git clone https://github.com/axcur/matematicas-aplicadas.git
cd matematicas-aplicadas
```

### 2. Crear y activar un entorno virtual (opcional pero recomendado)
```bash
# En Windows (PowerShell)
python -m venv .venv
.venv\Scripts\Activate.ps1
```

### 3. Instalar dependencias
```bash
pip install -r requirements.txt
```

### 4. Iniciar Jupyter Notebook / JupyterLab
```bash
jupyter notebook
```
o abrir la carpeta directamente en **VS Code** con la extensión de Jupyter instalada.
