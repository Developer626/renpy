# In this file, we have an example of replacing the default menu with
# a custom one. This new menu consists of a series of centered
# buttons, with dialogue appearing in a narration window.

# You can try this one out by dropping it right into the game
# directory.

# The code that implements button menus.
init:
    python:
        style.create('button', 'button')
        style.create('button_text', 'button_text')

        def menu(menuitems):

            narration = None

            ui.keymousebehavior()

            ui.window(style='menu_window')
            ui.vbox(xanchor='center', xpos=0.5)

            for label, value in menuitems:
                if value is None:
                    narration = label
                    continue

                ui.textbutton(label,
                              style="button",
                              text_style="button_text",
                              clicked=ui.returns(value))

            ui.close()

            if narration:
                narrator(narration, interact=False)

            rv = ui.interact()
            renpy.checkpoint()
            return rv

# Styles to make button menus look good.
init 1:
    python hide:
        style.menu_window.background = None
        style.menu_window.yminimum = 0
        style.menu_window.ypos = 0.40
        style.menu_window.yanchor = 'center'
        style.menu_window.xfill = True

        style.button.background = Solid((0, 0, 255, 128))
        style.button.xfill = True
        style.button.top_padding = 5
        style.button.bottom_margin = 5

        style.button_text.xpos = 0.5
        style.button_text.xanchor = 'center'

        style.button_text.hover_color = (255, 255, 0, 255)
        style.button_text.idle_color = (255, 255, 255, 255)
        
    
        
