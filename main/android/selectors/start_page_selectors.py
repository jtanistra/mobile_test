from attrdict import AttrDict
from selenium.webdriver.common.by import By

ELEMENTS = AttrDict({
    "start_arrow": (By.ID, 'com.silvair.app:id/start'),
    "logo": (By.XPATH, '//android.widget.FrameLayout[1]/android.widget.ImageView[1]'),
    "terms_conditions": (By.ID, 'com.silvair.app:id/terms_conditions')
    }
)
