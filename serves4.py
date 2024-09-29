from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager , Screen
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.dropdownitem import MDDropDownItem
#from kiv_garden.mapviewy import MapView, MapMarker
from geopy.geocoders import Nominatim
from kivymd.uix.list import ThreeLineAvatarListItem,ImageLeftWidget
from faker import Faker 
import random 
import webview
import json
import requests 
from kivy.uix.scrollview import ScrollView
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivymd.uix.dialog import MDDialog  
from kivy.uix.filechooser import FileChooserIconView 
from kivymd.uix.button import MDRectangleFlatButton  
from kivymd.uix.textfield import MDTextField 
from kivy.properties import ObjectProperty 
KV = '''
ScreenManager:
    size_hint: None, None  
    size: 400, 600
    MainScreen:
    SecondScreen:
    ThreeScreen:
    FourScreen:
    FiveScreen:
    SixScreen:
    SevenScreen:
    EightScreen:
    NineScreen:
    TenScreen:
<MainScreen>:
    name:'one'
    Image:  
        source: 'serves1.png' 
        pos_hint: {"center_x": 0.5, "center_y": 0.9}
        size_hint_x: None
        width: dp(300)  
        height: dp(300)     
    MDLabel:  
        text: "Login" 
        widget_position:"center"
        pos_hint: {"center_x": 0.8, "center_y": 0.7}
        mode: "round"
        size_hint_x: None
        width: dp(300)  
        height: dp(60)  
    MDTextField:
        hint_text: "user name"
        widget_position:"center"
        pos_hint: {"center_x": 0.5, "center_y": 0.6}
        mode: "round"
        size_hint_x: None
        width: dp(300)  
        height: dp(60) 
    MDTextField:
        hint_text: "password"
        pos_hint: {"center_x": 0.5, "center_y": 0.5}
        mode: "round"
        size_hint_x: None
        width: dp(300)  
        height: dp(60)      
    MDRaisedButton:
        text: "submit"
        pos_hint: {"center_x": 0.5, "center_y": 0.4}
        md_bg_color: app.theme_cls.primary_dark 
        mode:"rectangle"    
        size_hint_x: None
        width: dp(70)  
        height: dp(40)        
    MDRaisedButton:
        text: "I not have accounte"
        on_release:app.changeScreen('second')
        pos_hint: {"center_x": 0.5, "center_y": 0.3}
        md_bg_color: app.theme_cls.primary_dark    
<SecondScreen>:
    name:'second'
    MDTextField:
        hint_text: "user name"
        pos_hint: {"center_x": 0.5, "center_y": 0.8}
        size_hint_x: None
        width: dp(300)  
        height: dp(60)
    MDTextField:
        hint_text: "password"
        pos_hint: {"center_x": 0.5, "center_y": 0.7}
        size_hint_x: None
        width: dp(300)  
        height: dp(60)          
    MDTextField:
        hint_text: "password confirmation"
        pos_hint: {"center_x": 0.5, "center_y": 0.6}
        size_hint_x: None
        width: dp(300)  
        height: dp(60) 
    MDTextField:
        hint_text: "mobile number"
        pos_hint: {"center_x": 0.5, "center_y": 0.5}
        size_hint_x: None
        width: dp(300)  
        height: dp(60)         
    MDRaisedButton:
        text: "create accounte"
        on_release:app.changeScreen('three')
        pos_hint: {"center_x": 0.5, "center_y": 0.4}
        md_bg_color: app.theme_cls.primary_dark           
    MDRaisedButton:
        text: "I have accounte"
        on_release:app.changeScreen('one')
        pos_hint: {"center_x": 0.5, "center_y": 0.3}
        md_bg_color: app.theme_cls.primary_dark 
<ThreeScreen>:
    name :'three'
    Image:  
        source: 'serves3.png' 
        pos_hint: {"center_x": 0.5, "center_y": 0.7}
        size_hint_x: None
        width: dp(400)  
        height: dp(300)        
    MDRaisedButton:
        text: "onlaine shopping"
        on_release:app.changeScreen('four')
        pos_hint: {"center_x": 0.5, "center_y": 0.65}
        md_bg_color: app.theme_cls.primary_dark 
        mode:"rectangle"    
        size_hint_x: None
        width: dp(70)  
        height: dp(40) 
    Image:  
        source: 'serves4.png' 
        pos_hint: {"center_x": 0.5, "center_y": 0.4}
        size_hint_x: None
        width: dp(400)  
        height: dp(300)          
    MDRaisedButton:
        text: "onlaine Delivery "
        on_release:app.changeScreen('five')
        pos_hint: {"center_x": 0.5, "center_y": 0.4}
        md_bg_color: app.theme_cls.primary_dark 
<FourScreen>:
    name:'four'  
    Image:  
        source: 'serves5.png' 
        pos_hint: {"center_x": 0.25, "center_y": 0.9}
        size_hint_x: None
        width: dp(150)  
        height: dp(150)          
    MDRaisedButton:
        text: "Restaurants "
        on_release:app.changeScreen('six')
        pos_hint: {"center_x": 0.25, "center_y": 0.9}
        md_bg_color: app.theme_cls.primary_dark 
    Image:  
        source: 'serves6.png' 
        pos_hint: {"center_x": 0.75, "center_y": 0.9}
        size_hint_x: None
        width: dp(150)  
        height: dp(150)          
    MDRaisedButton:
        text: "Sweets "
        on_release:app.changeScreen('')
        pos_hint: {"center_x": 0.75, "center_y": 0.9}
        md_bg_color: app.theme_cls.primary_dark      
    Image:  
        source: 'serves7.png' 
        pos_hint: {"center_x": 0.25, "center_y": 0.6}
        size_hint_x: None
        width: dp(150)  
        height: dp(150)          
    MDRaisedButton:
        text: "Vegetables&fruits "
        on_release:app.changeScreen('four')
        pos_hint: {"center_x": 0.25, "center_y": 0.6}
        md_bg_color: app.theme_cls.primary_dark 
    Image:  
        source: 'serves9.png' 
        pos_hint: {"center_x": 0.75, "center_y": 0.6}
        size_hint_x: None
        width: dp(150)  
        height: dp(150)          
    MDRaisedButton:
        text: "Supermarket"
        on_release:app.changeScreen('four')
        pos_hint: {"center_x": 0.75, "center_y": 0.6}
        md_bg_color: app.theme_cls.primary_dark    
    Image:  
        source: 'serves8.png' 
        pos_hint: {"center_x": 0.25, "center_y": 0.3}
        size_hint_x: None
        width: dp(150)  
        height: dp(150)          
    MDRaisedButton:
        text: "Gifts"
        on_release:app.changeScreen('four')
        pos_hint: {"center_x": 0.25, "center_y": 0.3}
        md_bg_color: app.theme_cls.primary_dark 
    Image:  
        source: 'serves10.png' 
        pos_hint: {"center_x": 0.75, "center_y": 0.3}
        size_hint_x: None
        width: dp(150)  
        height: dp(150)          
    MDRaisedButton:
        text: "Clothes "
        on_release:app.changeScreen('seven')
        pos_hint: {"center_x": 0.75, "center_y": 0.3}
        md_bg_color: app.theme_cls.primary_dark    
    MDRaisedButton:
        text: "Back"
        on_release:app.changeScreen('three')
        pos_hint: {"center_x": 0.5, "center_y": 0.15}
        md_bg_color: app.theme_cls.primary_dark                       
<FiveScreen>:
    name:'five'
    MDLabel:  
        text: "Source" 
        widget_position:"center"
        pos_hint: {"center_x": 0.25, "center_y": 0.8}
        size_hint_x: None
        width: dp(150)  
        height: dp(60) 
    MDTextField:
        hint_text: "Region"
        widget_position:"center"
        pos_hint: {"center_x": 0.25, "center_y": 0.7}
        size_hint_x: None
        width: dp(150)  
        height: dp(60)               
    MDTextField:
        hint_text: "street"
        widget_position:"center"
        pos_hint: {"center_x": 0.25, "center_y": 0.6}
        size_hint_x: None
        width: dp(150)  
        height: dp(60) 
    MDTextField:
        hint_text: "Build"
        widget_position:"center"
        pos_hint: {"center_x": 0.25, "center_y": 0.5}
        size_hint_x: None
        width: dp(150)  
        height: dp(60) 
    MDLabel:  
        text: "Destination" 
        widget_position:"center"
        pos_hint: {"center_x": 0.75, "center_y": 0.8}
        size_hint_x: None
        width: dp(150)  
        height: dp(60)         
    MDTextField:
        hint_text: "Region"
        widget_position:"center"
        pos_hint: {"center_x": 0.75, "center_y": 0.7} 
        size_hint_x: None
        width: dp(150)  
        height: dp(60)                  
    MDTextField:
        hint_text: "street"
        widget_position:"center"
        pos_hint: {"center_x": 0.75, "center_y": 0.6}
        size_hint_x: None
        width: dp(150)  
        height: dp(60)         
    MDTextField:
        hint_text: "Build"
        widget_position:"center"
        pos_hint: {"center_x": 0.75, "center_y": 0.5}
        size_hint_x: None
        width: dp(150)  
        height: dp(60)  
    MDRaisedButton:
        text: "Request"
        on_release:app.changeScreen('five')
        pos_hint: {"center_x": 0.5, "center_y": 0.35}
        md_bg_color: app.theme_cls.primary_dark         
<SixScreen>:
    name:'six'
    MDRaisedButton: 
        text: "AlBake" 
        on_release:app.changeScreen('seven')        
        pos_hint: {"center_x": 0.4, "center_y": 0.8}
        size_hint_x: None
        width: dp(150)  
        height: dp(60)    
    Image:  
        source: 'serves11.png' 
        pos_hint: {"center_x": 0.8, "center_y": 0.8}
        size_hint_x: None
        width: dp(150)  
        height: dp(150)  
    MDRaisedButton:  
        text: "Dajajtee"
        on_release:app.changeScreen('seven')         
        pos_hint: {"center_x": 0.4, "center_y": 0.6}
        size_hint_x: None
        width: dp(150)  
        height: dp(60)    
    Image:  
        source: 'serves11.png' 
        pos_hint: {"center_x": 0.8, "center_y": 0.6}
        size_hint_x: None
        width: dp(150)  
        height: dp(150)
    MDRaisedButton:  
        text: "Baraka" 
        on_release:app.changeScreen('seven')        
        pos_hint: {"center_x": 0.4, "center_y": 0.4}
        size_hint_x: None
        width: dp(150)  
        height: dp(60)            
    Image:  
        source: 'serves11.png' 
        pos_hint: {"center_x": 0.8, "center_y": 0.4}
        size_hint_x: None
        width: dp(150)  
        height: dp(150)                                                        

<SevenScreen>:
    name:'seven'
    MDRaisedButton: 
        text: "Shaworma" 
        pos_hint: {"center_x": 0.2, "center_y": 0.8} 
        mode: "rectangle"  
        size_hint_x: None  
        width: dp(150)  
        height: dp(30)  
        md_bg_color: 1, 1, 1, 1  
        text_color: 1, 0.647, 0         
    MDLabel:  
        text: "30000" 
        pos_hint: {"center_x": 0.65, "center_y": 0.8}
        size_hint_x: None
        width: dp(150)  
        height: dp(60)
    Image:  
        source: 'serves11.png' 
        pos_hint: {"center_x": 0.8, "center_y": 0.8}
        size_hint_x: None
        width: dp(150)  
        height: dp(150)           
    MDRaisedButton:  
        text: "Next"  
        on_release:app.changeScreen('eight')  
        pos_hint: {"center_x": 0.5, "center_y": 0.2}
        size_hint_x: None
        width: dp(130)  
        height: dp(130) 
<EightScreen>:
    name:'eight'
    MDLabel:  
        text: "Total:" 
        pos_hint: {"center_x": 0.5, "center_y": 0.7}
        size_hint_x: None
        width: dp(150)  
        height: dp(60)
    MDLabel:  
        text: "30000" 
        pos_hint: {"center_x": 0.7, "center_y": 0.7}
        size_hint_x: None
        width: dp(150)  
        height: dp(60)
    MDRaisedButton:  
        text: "Next"  
        on_release:app.changeScreen('nine')  
        pos_hint: {"center_x": 0.5, "center_y": 0.5}
        size_hint_x: None
        width: dp(130)  
        height: dp(130) 
<NineScreen>:
    name:'nine'   
    MDLabel:  
        text: "Destination" 
        widget_position:"center"
        pos_hint: {"center_x": 0.5, "center_y": 0.8}
        size_hint_x: None
        width: dp(150)  
        height: dp(60)         
    MDTextField:
        hint_text: "Region"
        widget_position:"center"
        pos_hint: {"center_x": 0.5, "center_y": 0.7} 
        size_hint_x: None
        width: dp(150)  
        height: dp(60)                  
    MDTextField:
        hint_text: "street"
        widget_position:"center"
        pos_hint: {"center_x": 0.5, "center_y": 0.6}
        size_hint_x: None
        width: dp(150)  
        height: dp(60)         
    MDTextField:
        hint_text: "Build"
        widget_position:"center"
        pos_hint: {"center_x": 0.5, "center_y": 0.5}
        size_hint_x: None
        width: dp(150)  
        height: dp(60)  
    MDRaisedButton:
        text: "Request"
        on_release:app.changeScreen('ten')
        pos_hint: {"center_x": 0.5, "center_y": 0.35}
        md_bg_color: app.theme_cls.primary_dark         
<TenScreen>:
    name:'ten'
    MDLabel:  
        text: "Delivery cost:" 
        pos_hint: {"center_x": 0.4, "center_y": 0.7}
        size_hint_x: None
        width: dp(150)  
        height: dp(60)
    MDLabel:  
        text: "5000" 
        pos_hint: {"center_x": 0.8, "center_y": 0.7}
        size_hint_x: None
        width: dp(150)  
        height: dp(60)
    MDRaisedButton:  
        text: "Confirm order"  
        on_release:app.changeScreen('ten')  
        pos_hint: {"center_x": 0.5, "center_y": 0.5}
        size_hint_x: None
        width: dp(200)  
        height: dp(130)    
'''
class MainScreen(Screen):
    pass
class SecondScreen(Screen):
    pass
class ThreeScreen(Screen):
    pass
class FourScreen(Screen):
    pass
class FiveScreen(Screen):
    pass
class SixScreen(Screen):
    pass
class SevenScreen(Screen):
    pass
class EightScreen(Screen):
    pass
class NineScreen(Screen):
    pass
class TenScreen(Screen):
    pass
class MainApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Orange"
        self.theme_cls.theme_style = "Light"
        self.saved_locations = []  # قائمة لحفظ المواقع
        return Builder.load_string(KV)
    def changeScreen(self, screen_name):
        self.root.current =screen_name

    def save_data(self):  
        restaurant_name = self.root.ids.restaurant_name.text  
        food_item = self.root.ids.food_item.text  
        price = self.root.ids.price.text  
        image_path = self.root.ids.restaurant_image.source  

        # هنا يمكنك إضافة الكود لحفظ البيانات في قاعدة بيانات أو ملف  
        print(f"اسم المطعم: {restaurant_name}, الصنف: {food_item}, السعر: {price}, مسار الصورة: {image_path}")  
    def add_text_field(self):  
        text_field = MDTextField(hint_text="Enter text here")  
        self.root.ids.input_container.add_widget(text_field)
         
    def local_latlng(self, country_code, coords_only=False):  
        # حرر هذا الجزء بحسب احتياجاتك  
        # هنا أنا أستخدم قيم عشوائية كمثال  
        latitude = random.uniform(-10, 10)  # إحداثيات عشوائية  
        longitude = random.uniform(100, 110)  # إحداثيات عشوائية  
        return latitude, longitude    
 
        #self.id_container = self.root.get_screen('four').ids.id_container  

    def open_map(self):  
        # إحداثيات لمواقع في محافظة دمشق  
        damascus_locations = [  
            (33.5138, 36.2765),  # مركز دمشق  
            (33.5163, 36.2915),  # قصر العدل  
            (33.5138, 36.2765),  # ساحة الأمويين  
            (33.5161, 36.2925),  # باب توما  
            (33.5111, 36.2769)   # سوق الحميدية  
        ]  
        
        # فتح الخريطة لكل موقع  
        for lat, lon in damascus_locations:  
            self.viewlocation(lat, lon)              
    def viewlocation(self, lat, lon):
        url = f"https://www.google.com/maps/@{lat},{lon},17z"
        print("open please wait")
        webview.create_window("Location", url=url)
        webview.start(debug=False)

        # حفظ المصدر والوجهة
        self.save_location(lat, lon)

    def save_location(self, lat, lon):  
        location = {"latitude": lat, "longitude": lon}  
        self.saved_locations.append(location)  

        if len(self.saved_locations) == 2:  
            # جلب معلومات المسافة والمدة من Google Maps API  
            self.get_distance_and_duration(self.saved_locations[0], self.saved_locations[1])  
            self.saved_locations = []  # إعادة تعيين القائمة بعد الحساب  

    def get_distance_and_duration(self, loc1, loc2):  
        # استبدل YOUR_API_KEY بمفتاح API الخاص بك  
        api_key = "AIzaSyDxx8q4TT8WJyalSBSm_ZFqYSqZ0hb-SHc"  
        origin = f"{loc1['latitude']},{loc1['longitude']}"  
        destination = f"{loc2['latitude']},{loc2['longitude']}"  
        url = f"https://maps.googleapis.com/maps/api/directions/json?origin={origin}&destination={destination}&key={api_key}"  

        response = requests.get(url)  
        data = response.json()  

        if data['status'] == 'OK':  
            distance = data['routes'][0]['legs'][0]['distance']['text']  
            duration = data['routes'][0]['legs'][0]['duration']['text']  
            print(f"Distance: {distance}, Duration: {duration}")  
        else:  
            print("Error fetching data from Google Maps API")  
if __name__ == "__main__":
    MainApp().run()