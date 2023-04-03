from engine.engine import Engine

class SternmanEngine(Engine):
    def _init_(self, warning_light_is_on):
        self.warning_light_is_on = warning_light_is_on
    
    def needs_service(self):
        if self.warning_light_is_on:
            return True
        else:
            return False