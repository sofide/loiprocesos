class OrderError(Exception):
    pass


def switch_order(element_1, element_2):
    """Switch 'orden' value between two elements if they are adjacent.

    Raise OrderError if the elements are not adjacent, or they are from different
    classes or units.
    """
    model_class, unidad = get_class_and_unit(element_1, element_2)

    if abs(element_1.orden - element_2.orden):
        update_order(model_class, unidad)
        element_1 = model_class.objects.get(pk=element_1.pk)
        element_2 = model_class.objects.get(pk=element_2.pk)

        if abs(element_1.orden - element_2.orden):
            msg = "Cannot switch order of {} and {} because they are not adjacent"
            raise OrderError(msg.format(element_1, element_2))

    orig_element_1_orden = element_1.orden
    orig_element_2_orden = element_2.orden

    element_1.orden = orig_element_2_orden
    element_2.orden = orig_element_1_orden

    element_1.save()
    element_2.save()


def get_class_and_unit(element_1, element_2):
    """Get class and unit from the received elements.

    Raise OrderError if the element are from different classes or units.
    """
    if element_1.__class__ != element_2.__class__:
        raise OrderError("{} and {} are from different classes.")

    if element_1.unidad != element_2.unidad:
        raise OrderError("{} and {} are from different units.")

    return element_1.__class__, element_1.unidad


def update_order(model, unidad):
    """
    Update de order of all elements of the given model and unit.
    """
    elements_to_order = model.objects.filter(unidad=unidad)

    for order, element in enumerate(elements_to_order):
        print("about to update {} from order {} to order {}".format(element, element.orden, order))
        element.orden = order
        element.save()
