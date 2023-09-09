from src.context.variables import WaypointKeys
from src.repo.minimap.core import get_waypoints


def set_context_waypoint_middleware(context):
    waypoints = get_waypoints(context.get_screenshot())
    context.set_waypoint(WaypointKeys.WAYPOINTS, waypoints)
    return context
