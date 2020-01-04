from wtforms import Form, FloatField, SelectField, validators
from math import pi

class InputForm(Form):

    bedrooms =  SelectField(
                       label = 'Number of Bedrooms', default = '6', choices =  \
                        [('1', '1'),('2','2'),('3', '3'),('4', '4'),('5', '5'),\
                        ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'),('10', '10')])


    waterfront = SelectField(
                       label = 'Waterfront View, No/Yes', default = '0',
                       choices = [('1', 'Yes'),('0','No')])

    view =      SelectField(
                       label = 'View from Property, <br> Index between 0 and 4', default = '3',
                      choices = [('0', '0'),('1', '1'),('2','2'),
                                 ('3', '3'), ('4','4')])


    grade =     SelectField(
                       label = 'Grade, Level of Construction <br> between 0 and 13', default = '6',
                        choices = [('1', '1'),('2','2'),('3', '3'),('4', '4'),('5', '5'),('6', '6'),
                                   ('7', '7'), ('8', '8'), ('9', '9'),('10', '10'), ('11','11'), ('12','12'),('13','13')])


    year = [(str(x), str(x)) for x in range(1900,2016)]

    yob =           SelectField(
                      label = 'Year of Build', default = '1980',
                      choices= year)

    columns_zipcode = ['98001', '98002', '98003', '98004', '98005',
       '98006', '98007', '98008', '98010', '98011', '98014', '98019', '98022',
       '98023', '98024', '98027', '98028', '98029', '98030', '98031', '98032',
       '98033', '98034', '98038', '98039', '98040', '98042', '98045', '98052',
       '98053', '98055', '98056', '98058', '98059', '98065', '98070', '98072',
       '98074', '98075', '98077', '98092', '98102', '98103', '98105', '98106',
       '98107', '98108', '98109', '98112', '98115', '98116', '98117', '98118',
       '98119', '98122', '98125', '98126', '98133', '98136', '98144', '98146',
       '98148', '98155', '98166', '98168', '98177', '98178', '98188', '98198',
       '98199']

    zipcodes =   [(str(x), str(x)) for x in columns_zipcode]

    zipcode =       SelectField(
                     label = 'Zipcode', default = '98148',
                     choices = zipcodes)

    sqft_living = FloatField(
                label = 'Living Area, sqft', default = 2300,
                validators=[validators.InputRequired()])

    # sqft_lot =  FloatField(
    #             label = 'Lot area, sqft', default = 2500,
    #             validators=[validators.InputRequired()])



    # sqft_basement = FloatField(
    #                    label = 'Basement area, sqft', default = 0,
    #                    validators=[validators.InputRequired()])
