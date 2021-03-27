import logging
import logging.config
import json

with open('log_config.json', 'r') as log_config_json:
    logging.config.dictConfig(json.load(log_config_json)['logging'])

logger = logging.getLogger('main')
logger.setLevel('DEBUG')


class Rectangle:
    def __init__(self, a: float, b: float):
        self.a = a
        self.b = b
        if self.a < 0 or self.b < 0:
            logger.warning(f"One value is < 0")
        else:
            logger.debug(f"New rectangle a: {a} b: {b}")

    def area(self) -> float:
        area = self.a * self.b
        logger.debug(f"Rectangle area : {area}")
        return area

    def perimeter(self) -> float:
        perimeter = 2 * (self.a + self.b)
        logger.debug(f"Rectangle perimeter : {perimeter}")
        return perimeter


test = Rectangle(-1.0, 4.0)
test.area()
