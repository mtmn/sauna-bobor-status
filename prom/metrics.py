from prometheus_client import Gauge

metric_water_temp = Gauge("shmu_water_temperature", "Water temperature in C")
metric_water_level = Gauge("shmu_water_level", "Water level in cm")
metric_bobor_capacity = Gauge("bobor_capacity", "Current people in Bobor")
metric_sauna_temp = Gauge("sauna_temperature", "Sauna temperature")
metric_sauna_door = Gauge("sauna_door_closed", "Sauna door closed status")

metric_shmu_last_updated = Gauge("shmu_last_updated", "Timestamp of last SHMU update")
metric_bobor_last_updated = Gauge(
    "bobor_last_updated", "Timestamp of last Bobor update"
)
metric_sauna_last_updated = Gauge(
    "sauna_last_updated", "Timestamp of last Sauna update"
)
