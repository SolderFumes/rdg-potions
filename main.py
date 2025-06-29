import tkinter as tk
running = True
def onclose():
    global running
    running = False
root = tk.Tk()
root.geometry = ('800x600')
root.title('rdg-potions')
root.protocol("WM_DELETE_WINDOW", onclose)
recipes = {
    'Luck':            ['Accrue',    'Abate'],
    'Protection':      ['Fervor',    'Ardor'],
    'Regeneration':    ['Virulent',  'Theriac'],
    'Healing':         ['Fervor',    'Accrue'],
    'Stats Up':        ['Tenebrous', 'Gambol'],
    'Swiftness':       ['Gambol',    'Skew'],
    'Warping':         ['Abate',     'Ichor'],
    'Resistance':      ['Vigor',     'Ardor'],
    'Brawn':           ['Vigor',     'Ichor'],
    'Affluence':       ['Virulent',  'Lucre'],
    'Jumping':         ['Cavort',    'Lucre'],
    'Chance':          ['Cavort',    'Skew'],
    'Sustaining':      ['Tenebrous', 'Theriac'],
    'Ice Resistance':  ['Luminous',  'Algid'],
    'Fire Resistance': ['Luminous',  'Torrid'],
    'Balance':         ['Torrid',    'Algid'],
}
potion_effects = {
    "Luck": "Gain 🍀 3; if you're the only player alive, gain 🍀 5 instead.",
    "Protection": "Gain ❤️ Max HP equal to 10 × World #.",
    "Regeneration": "Regenerate ❤️ HP equal to the Room #.",
    "Healing": "Heal ❤️ HP equal to 10 × World #.",
    "Stats Up": "Boost your stats when consumed.",
    "Swiftness": "Gain ➔ 3.",
    "Warping": "Warp forwards or backwards a world. (The direction this potion will warp in is only visible when picked up!)",
    "Resistance": "Gain 🛡 1 if you have no 🛡 Defense; then gain 🛡 2.",
    "Brawn": "Gain 💪 Strength equal to triple the World # when used.",
    "Affluence": "Gain 💰 Circuits equal to the Room #. Cannot be used in the room in which you acquired it.",
    "Jumping": "Gain ↑ 20.",
    "Chance": "Gain the effect of a random potion; then heal ❤️ 25.",
    "Sustaining": "Gain 💛 5; then heal ❤️ 25.",
    "Ice Resistance": "Gain immunity to water hazards, freezing, and icicles. Lasts for thirty rooms.",
    "Fire Resistance": "Gain immunity to fire hazards and taking burn damage. Lasts for thirty rooms.",
    "Balance": "Resets your ➔ Walkspeed and ↑ Jump power if they are below average; then gain ➔ 1 and ↑ 5."
}
potion_widgets = {} #potionName : widget reference
#pre-load images since we have to redraw buttons every time
potion_images = {name: tk.PhotoImage(file=f'./images/{name}.gif') for name in recipes.keys()}
possibleBerries = ['Fervor', 'Ardor', 'Virulent', 'Theriac', 'Accrue', 'Tenebrous', 'Gambol', 'Skew', 'Abate', 'Ichor', 'Vigor', 'Lucre', 'Cavort', 'Luminous', 'Algid', 'Torrid']
hadBerries = []
images = {}

def check_craftable():
    retList = []
    for name, recipe in recipes.items():
        if recipe[0] in hadBerries and recipe[1] in hadBerries:
             retList.append(name)
    return retList

def add_berry(name, button):
    if name not in hadBerries:
        hadBerries.append(name)
        # highlight button
        button.config(
            bd=4,
            highlightthickness=4,
            highlightbackground='green',
            highlightcolor='green'
        )

    else:
        hadBerries.remove(name)
        button.config(
            bd=0,
            highlightthickness=0
        )


#berry display area
berry_frame = tk.Frame(root)
berry_frame.grid(row=0, column=0, sticky="nw", padx=10, pady=10)

#display each berry button
for index, berry in enumerate(possibleBerries):
    img = tk.PhotoImage(file=f'./images/{berry}.gif')
    images[berry] = img # keep a reference of every PhotoImage object so it isn't garbage collected

    btn = tk.Button(berry_frame, image=img, text=berry, compound='top',padx=5,pady=5)
    btn.config(command=lambda b=berry, w=btn: add_berry(b,w))

    btn.grid(row=index // 4, column=index % 4, padx=5, pady=5)

#potion display area
potion_frame = tk.Frame(root)
potion_frame.grid(row=0, column=1, sticky='nw', padx=20, pady=10)


# main loop
while True:
    if not running:
        break
    root.update_idletasks()
    root.update()

    craftable = check_craftable()
    # delete any potions that are not longer craftable
    # traverse a copy of potion_widgets to avoid changing size of dict during iteration
    for pot in list(potion_widgets.keys()):
        if pot not in craftable:
            potion_widgets[pot].destroy()
            del potion_widgets[pot]
            print("removing",pot,craftable)

    for row, pot_name in enumerate(craftable):
        if pot_name not in potion_widgets:
            print("adding",pot_name,craftable)
            img = potion_images[pot_name]
            #subframe for each item
            item = tk.Frame(potion_frame)
            item.grid(row=row, column=0, sticky="w", pady=5)

            #potion image
            lbl_img = tk.Label(item, image=img)
            lbl_img.grid(row=0, column=0)

            #potion desc
            lbl_txt = tk.Label(item, text=f"{pot_name}\n{potion_effects[pot_name]}\n{recipes[pot_name][0]}, {recipes[pot_name][1]}",
                               justify="left", anchor="w")
            lbl_txt.grid(row=0, column=1, padx=10)

            potion_widgets[pot_name] = item
        else:
            potion_widgets[pot_name].grid_configure(row=row)


print(hadBerries)
