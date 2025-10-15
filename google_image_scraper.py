from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://www.google.com/search?q=python+course+for+beginners+images&sca_esv=853236ac3d6bce34&rlz=1C1CHBF_enPK1140PK1140&udm=2&biw=1536&bih=730&sxsrf=AE3TifMhi41mNOXBV6GtvSZrOcCSp7BvdA%3A1760550370397&ei=4t3vaKuDGN67hbIPjZf1EA&ved=0ahUKEwir_L6b4aaQAxXeXUEAHY1LHQIQ4dUDCBE&uact=5&oq=python+course+for+beginners+images&gs_lp=Egtnd3Mtd2l6LWltZyIicHl0aG9uIGNvdXJzZSBmb3IgYmVnaW5uZXJzIGltYWdlc0inF1CJBVj_FXACeACQAQCYAecBoAGtCqoBBTAuNC4zuAEDyAEA-AEBmAIEoAKdA8ICBxAjGMkCGCfCAgYQABgHGB7CAgUQABiABMICBBAAGB7CAgYQABgIGB6YAwCIBgGSBwUyLjEuMaAH5w2yBwUwLjEuMbgHhgPCBwUyLTMuMcgHHw&sclient=gws-wiz-img")
time.sleep(5)

scraper = driver.find_elements(By.TAG_NAME,"img")

images_URL=[]
for i in scraper:
    images = i.get_attribute("src")
    if images:
        images_URL.append(images)

for i in images_URL:
      with open("storage.txt","a")as file:
        file.write(i + "\n")
    # print(i + "\n")

print(len(images_URL))

driver.quit()