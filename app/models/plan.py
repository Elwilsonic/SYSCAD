from dataclasses import dataclass

@dataclass(init=False, repr=True, eq=True)
class Plan():
    nombre: str
    fecha_inicio: int
    fecha_fin: int
    observacion: str