from classifier.classifier import classify

from vendors.paloalto.dashboard import parse_dashboard
from vendors.paloalto.disk import parse_disk
from vendors.paloalto.resource import parse_resource
from vendors.paloalto.environment import parse_environment


def parse(text: str):

    screenshot_type = classify(text)

    if screenshot_type == "dashboard":
        return parse_dashboard(text)

    elif screenshot_type == "disk":
        return parse_disk(text)

    elif screenshot_type == "resource":
        return parse_resource(text)

    elif screenshot_type == "environment":
        return parse_environment(text)

    return {}