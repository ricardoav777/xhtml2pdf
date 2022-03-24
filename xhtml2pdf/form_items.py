from reportlab.pdfgen import canvas

from xhtml2pdf.util import getColor, getSize, getCoords


class Props:
    """ Class to manage a property map and insert the attributes to each form item """
    def __init__(self, instance):
        self.prop_map = [("fillColor", getColor),("borderColor",getColor),("textColor",getColor),("borderWidth",int),("borderStyle",str),
                         ("x", int),("y", int), ("tooltip", str), ("name", str),("annotationFlags", str),("fieldFlags", str),
                         ("forceBorder", bool),("relative", bool), ("dashLen", int)]

    def add_prop(self, data):
        self.prop_map += data


class BaseItem:
    """ Base class for all form items"""

    def set_properties(self, data, props=None):
        """Sets the properties from data and included in prop map, to an attribute of the class"""
        if props is None:
            props = Props(self)

        for key, fnc in props.prop_map:
            if key in data:
                try:
                    value = fnc(data[key])

                    if value is not None:
                        self.__setattr__(key, value)
                except:
                    continue

    def set_pos(self, param):
        """ Sets the X and Y position of the page where the form item is going to be rendered,
        and returns it to outer method to assign it to the following form item, still needs work to be done
        """
        new_x, new_y = None, None
        if 'x' in param and 'y' in param:
            self.__setattr__('x', param['x'])
            self.__setattr__('y', param['y'])
            self_dict = self.__dict__
            if 'size' in self_dict:
                new_x = self_dict['size'] + self_dict['x']
                new_y = self_dict['size'] + self_dict['y']

            else:
                new_x = self_dict['width'] + self_dict['x']
                new_y = self_dict['height'] + self_dict['y']
        return new_x, new_y


class ChoiceItem(BaseItem):
    def __init__(self):
        super().__init__()

    def set_properties(self, data, props=None):
        props = Props(self)
        props.add_prop([("width", getSize)])
        props.add_prop([("height", getSize)])
        props.add_prop([("value", str)])
        props.add_prop([("fontName", str)])
        props.add_prop([("fontSize", int)])
        super().set_properties(data, props=props)

    def create(self, canvas):
        form = canvas.acroForm
        form.textfield(**dict(self.__dict__))

    def set_pos(self, param):
        return super().set_pos(param)


class CheckboxItem(BaseItem):
    def __init__(self):
        super().__init__()

    def set_properties(self, data, props=None):
        props = Props(self)
        props.add_prop([("checked", bool)])
        props.add_prop([("buttonStyle", str)])
        props.add_prop([("size", getSize)])
        super().set_properties(data, props=props)

    def create(self, canvas):
        form = canvas.acroForm
        form.checkbox(**dict(self.__dict__))

    def set_pos(self, param):
        return super().set_pos(param)

class ListboxItem(BaseItem):
    def __init__(self):
        super().__init__()

    def set_properties(self, data, props=None):
        props = Props(self)
        props.add_prop([("width", getSize)])
        props.add_prop([("height", getSize)])
        props.add_prop([("value", str)])
        props.add_prop([("fontName", str)])
        props.add_prop([("fontSize", int)])
        props.add_prop([("options", list)])
        super().set_properties(data, props=props)

    def create(self, canvas):
        form = canvas.acroForm
        form.listbox(**dict(self.__dict__))

    def set_pos(self, param):
        return super().set_pos(param)


class RadioItem(BaseItem):
    def __init__(self):
        super().__init__()

    def set_properties(self, data, props=None):
        props = Props(self)
        props.add_prop([("value", str)])
        props.add_prop([("selected", bool)])
        props.add_prop([("buttonStyle", str)])
        props.add_prop([("size", getSize)])
        props.add_prop([("shape", str)])
        super().set_properties(data, props=props)

    def create(self, canvas):
        form = canvas.acroForm
        form.radio(**dict(self.__dict__))

    def set_pos(self, param):
        return super().set_pos(param)


class TextfieldItem(BaseItem):
    def __init__(self):
        super().__init__()

    def set_properties(self, data, props=None):
        props = Props(self)
        props.add_prop([("width", getSize)])
        props.add_prop([("height", getSize)])
        props.add_prop([("value", str)])
        props.add_prop([("fontName", str)])
        props.add_prop([("fontSize", int)])
        super().set_properties(data, props=props)

    def create(self, canvas):
        form = canvas.acroForm
        form.textfield(**dict(self.__dict__))

    def set_pos(self, param):
        return super().set_pos(param)
