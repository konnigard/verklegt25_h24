"""Utility functions for sorting data in Icelandic order"""
import locale

def setup_icelandic_locale():
    """Set up Icelandic locale for sorting"""
    try:
        locale.setlocale(locale.LC_ALL, 'is_IS.UTF-8')
    except locale.Error:
        try:
            locale.setlocale(locale.LC_ALL, 'is_IS')
        except locale.Error:
            # Fallback to default if Icelandic locale not available
            pass

def sort_by_name(items, name_attr):
    """Sort a list of objects by a name attribute using Icelandic collation

    Args:
        items: List of objects to sort
        name_attr: Name of the attribute to sort by (string)

    Returns:
        Sorted list
    """
    try:
        return sorted(items, key=lambda item: locale.strxfrm(getattr(item, name_attr)))
    except (locale.Error, AttributeError):
        # Fallback to regular sorting if locale fails
        return sorted(items, key=lambda item: getattr(item, name_attr))

# Initialize locale when module is imported
setup_icelandic_locale()
