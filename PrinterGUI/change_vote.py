import gui

def change1(self):
    self.controller.shared_data['1stplace'].set(self.controller.shared_data['1stplace'].get())
    self.controller.shared_data['2ndplace'].set(self.controller.shared_data['2ndplace'].get())
    self.controller.shared_data['3rdplace'].set(self.controller.shared_data['3rdplace'].get())
    self.controller.show_frame('PageTwo')

def change2(self):
    self.controller.shared_data['1stplace'].set(self.controller.shared_data['1stplace'].get())
    self.controller.shared_data['2ndplace'].set(self.controller.shared_data['2ndplace'].get())
    self.controller.shared_data['3rdplace'].set(self.controller.shared_data['3rdplace'].get())
    self.controller.show_frame('PageThree')

def change3(self):
    self.controller.shared_data['1stplace'].set(self.controller.shared_data['1stplace'].get())
    self.controller.shared_data['2ndplace'].set(self.controller.shared_data['2ndplace'].get())
    self.controller.shared_data['3rdplace'].set(self.controller.shared_data['3rdplace'].get())
    self.controller.show_frame('PageFour')
    
# def change1(self):
#     if self.controller.shared_data['1stplace'].get() != 'No Vote' and 
#        self.controller.shared_data['1stplace'].get() != 'Project 1' and 
#        self.controller.shared_data['1stplace'].get() != 'Project 2' and 
#        self.controller.shared_data['1stplace'].get() != 'Project 3' and 
#        self.controller.shared_data['1stplace'].get() != 'Project 4':
#             self.controller.shared_data['1stplace'].set('Others')

#     if self.controller.shared_data['2ndplace'].get() != 'No Vote' and 
#        self.controller.shared_data['2ndplace'].get() != 'Project 1' and 
#        self.controller.shared_data['2ndplace'].get() != 'Project 2' and 
#        self.controller.shared_data['2ndplace'].get() != 'Project 3' and 
#        self.controller.shared_data['2ndplace'].get() != 'Project 4':
#             self.controller.shared_data['2ndplace'].set('Others')

#     if self.controller.shared_data['3rdplace'].get() != 'No Vote' and 
#        self.controller.shared_data['3rdplace'].get() != 'Project 1' and 
#        self.controller.shared_data['3rdplace'].get() != 'Project 2' and 
#        self.controller.shared_data['3rdplace'].get() != 'Project 3' and 
#        self.controller.shared_data['3rdplace'].get() != 'Project 4':
#             self.controller.shared_data['3rdplace'].set('Others')

#     self.controller.show_frame('PageTwo')

# def change2(self):
#     if self.controller.shared_data['2ndplace'].get() != 'No Vote' and 
#        self.controller.shared_data['2ndplace'].get() != 'Project 1' and 
#        self.controller.shared_data['2ndplace'].get() != 'Project 2' and 
#        self.controller.shared_data['2ndplace'].get() != 'Project 3' and 
#        self.controller.shared_data['2ndplace'].get() != 'Project 4':
#             self.controller.shared_data['2ndplace'].set('Others')

#     if self.controller.shared_data['3rdplace'].get() != 'No Vote' and 
#        self.controller.shared_data['3rdplace'].get() != 'Project 1' and 
#        self.controller.shared_data['3rdplace'].get() != 'Project 2' and 
#        self.controller.shared_data['3rdplace'].get() != 'Project 3' and 
#        self.controller.shared_data['3rdplace'].get() != 'Project 4':
#             self.controller.shared_data['3rdplace'].set('Others')

#     self.controller.show_frame('PageThree')

# def change3(self):
#     if self.controller.shared_data['3rdplace'].get() != 'No Vote' and 
#        self.controller.shared_data['3rdplace'].get() != 'Project 1' and 
#        self.controller.shared_data['3rdplace'].get() != 'Project 2' and 
#        self.controller.shared_data['3rdplace'].get() != 'Project 3' and 
#        self.controller.shared_data['3rdplace'].get() != 'Project 4':
#             self.controller.shared_data['3rdplace'].set('Others')

#     self.controller.show_frame('PageFour')

