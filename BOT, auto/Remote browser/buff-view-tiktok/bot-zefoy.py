from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.firefox.options import Options
from webdriver_manager.firefox import GeckoDriverManager
import os, sys
from tkinter import messagebox


driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())



