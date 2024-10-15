import            pyautogui                   as    pag
from pyautogui import  click                  as    click
from pyautogui import  locateCenterOnScreen   as    buscar
from time      import  sleep                  as    sleep
from pyautogui import  ImageNotFoundException as    cant_find_img

pag.sleep(0.3)
pag.FAILSAFE = True
#UHs = str("")
UHs = str(input("número do UH: ") )

UHs = buscar('projetoautomacao_pngs_\\PNGS-APS\\' + UHs + '.png')
#UHs[0]
#x, y = UHs
click(UHs)
print(UHs)
sleep(0.7)

extrato_conta = buscar('projetoautomacao_pngs_\\lancamento_IMGS\\extrato_conta.png')
click(extrato_conta)

sleep(2)

Extra = buscar('projetoautomacao_pngs_\\lancamento_IMGS\\Extra.png')
click(Extra)
if cant_find_img():
    particular = buscar('projetoautomacao_pngs_\\lancamento_IMGS\\particular.png')
    click(particular)

sleep(0.7)

def lancamento_efetivo():
    lancar_item = buscar('projetoautomacao_pngs_\\lancamento_IMGS\\lancar_item_img.png')
    click(lancar_item)

    sleep(0.7)

    pdv = buscar('projetoautomacao_pngs_\\lancamento_IMGS\\PDV_img.png')
    click(pdv)
    PDV = [str(input("PDV: ")).strip() for I in PDV.split(',')]
    if "consumação" == PDV():
        print("hello world, its working!")

 # a = b


    sleep(0.7)
    
    










# buscar('projetoautomacao_pngs_\\lancamento_IMGS\\  .png')
# buscar('projetoautomacao_pngs_\\lancamento_IMGS\\  .png')
# buscar('projetoautomacao_pngs_\\lancamento_IMGS\\  .png')
# buscar('projetoautomacao_pngs_\\lancamento_IMGS\\  .png')
# buscar('projetoautomacao_pngs_\\lancamento_IMGS\\  .png')
# buscar('projetoautomacao_pngs_\\lancamento_IMGS\\  .png')
# buscar('projetoautomacao_pngs_\\lancamento_IMGS\\  .png')







#for "" in UHs():
 #   do this: trlalala

#N_comanda = str(input("número da comanda: "))
#pdv = str(input("PDV: "))

#ITEM = str(input("Item: "))
#qntd_item = str(input("quantidade do item: "))

#lancar_isso_isso = list[UH, N_comanda, pdv, ITEM, qntd_item]

#print(lancar_isso_isso)

# UH LOCALIZADOR E CLICK
#sleep(0.7)
#UH_loc = buscar('projetoautomacao_pngs_\\PNGS-APS\\' + UHs + '.png') 
#click('UH_loc')
#sleep(0.7)




# sleep(1)
# menu_inicial = buscar('projetoautomacao_pngs_\\lancamento_IMGS\\mapa_UHs_IMG', confidence=0.8)
# click(menu_inicial)

# print("Good Work!")





