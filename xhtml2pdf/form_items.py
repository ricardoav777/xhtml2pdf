from reportlab.pdfgen import canvas

from xhtml2pdf.util import getColor


class Props:

    def __init__(self, instance):
        self.prop_map = [("fillColor", getColor),("borderColor",getColor),("textColor",getColor),("borderWidth",int),("borderStyle",str),
                         ("x", int),("y", int), ("tooptip", str), ("name", str),("annotationFlags", str),("fieldFlags", str),
                         ("forceBorder", bool),("relative", bool), ("dashLen", int)]

    def add_prop(self, data):
        self.prop_map += data


class BaseItem:
    def load_extra_data(self):
        pass

    def set_properties(self, data, props=None):
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


class ChoiceItem(BaseItem):
    def __init__(self):
        super().__init__()

    def set_properties(self, data, props=None):
        props = Props(self)
        props.add_prop([("width", int)])
        props.add_prop([("height", int)])
        props.add_prop([("value", str)])
        props.add_prop([("fontName", str)])
        props.add_prop([("fontSize", int)])
        super().set_properties(data, props=props)


class CheckboxItem(BaseItem):
    def __init__(self):
        super().__init__()

    def set_properties(self, data, props=None):
        props = Props(self)
        props.add_prop([("width", int)])
        props.add_prop([("checked", bool)])
        props.add_prop([("buttonStyle", str)])
        props.add_prop([("size", int)])
        super().set_properties(data, props=props)


class ListboxItem(BaseItem):
    def __init__(self):
        super().__init__()

    def set_properties(self, data, props=None):
        props = Props(self)
        props.add_prop([("width", int)])
        props.add_prop([("height", int)])
        props.add_prop([("value", str)])
        props.add_prop([("fontName", str)])
        props.add_prop([("fontSize", int)])
        super().set_properties(data, props=props)


class RadioItem(BaseItem):
    def __init__(self):
        super().__init__()

    def set_properties(self, data, props=None):
        props = Props(self)
        props.add_prop([("selected", bool)])
        props.add_prop([("buttonStyle", str)])
        props.add_prop([("size", int)])
        props.add_prop([("shape", str)])
        super().set_properties(data, props=props)


class TextfieldItem(BaseItem):
    def __init__(self):
        super().__init__()

    def set_properties(self, data, props=None):
        props = Props(self)
        props.add_prop([("width", int)])
        props.add_prop([("height", int)])
        props.add_prop([("value", str)])
        props.add_prop([("fontName", str)])
        props.add_prop([("fontSize", int)])
        super().set_properties(data, props=props)

    def create(self):
        pass
        # needs to create the form with the properties from above
        # form = canvas.acroform(all properties from prop_map)
        # return form
