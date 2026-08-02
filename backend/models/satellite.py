from pydantic import BaseModel


class PlanetScene(BaseModel):
    id: str
    published: str
    stage: str
    quality: str
    cloud: float


class LatestScene(BaseModel):
    scene: PlanetScene
    assets: list[str]