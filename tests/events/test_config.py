"""
Test configuration for FailureTracker.
"""


def get_test_config():
    """Return test configuration for FailureTracker."""
    return {
        "tool_family_thresholds": {
            "default": {
                "Filesystem": 3,
                "Notion": 3,
                "ollama": 3,
            },
            "domain_1_professional": {
                "Filesystem": 2,  # Lower threshold for professional domain
                "Notion": 4,
            },
        }
    }
