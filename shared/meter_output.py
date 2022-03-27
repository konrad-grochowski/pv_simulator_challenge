from dataclasses import dataclass

@dataclass
class MeterOutput:
    timestamp_seconds: int
    meter_value: float
