
function resize_input(){
    // Resize text input based on entry
    INPUT_TEXT.style.height = '30px';
    INPUT_TEXT.style.height = `${INPUT_TEXT.scrollHeight + 2}px` ;
}


function scroll_down(){
    // Moves scroll box down to lowest
    CHATBOX.scrollTop = CHATBOX.scrollHeight;
}

function changeSettingsDisplay(button){
    const panelName = button.dataset.panel;
    const templateId = `${panelName}-panel`;
    const template = document.getElementById(templateId);

    const display =  document.getElementById('settings-display');
    const panels = display.querySelectorAll('[class="display"]');
    
    panels.forEach(panel => {
        panel.style.display = 'none';
    })
    template.style.display = 'block';
}

const Settings = {
    defaults: {
        primaryColor: '#0C0F11',
        fontColor: '#adadad',
        use_local: true,
        model: 'deepseek-v3.1:671b-cloud',
        api_key: '000'
    },

    getStorage() {
    try {
      // Try localStorage first
      localStorage.getItem('appSettings');
      return localStorage;
    } catch (e) {
      // Fallback to sessionStorage
      localStorage.setItem('appSettings');
      return localStorage;
    }
  },

  init() {
    const storage = this.getStorage();
    const saved = storage.getItem('appSettings');


    this.current = saved ? JSON.parse(saved) : { ...this.defaults };
    this.applyAll();

    console.log(JSON.parse(saved), saved);

    pywebview.api.log("Settings.init(): " + storage, 10);
  },
  
  get(key) {
    return this.current[key] ?? this.defaults[key]; // Auto-fallback
  },
  
  set(key, value) {
    this.current[key] = value;
    localStorage.setItem('appSettings', JSON.stringify(this.current));
    this.apply(key, value);
  },
  
  apply(key, value) {
    const actualValue = value ?? this.defaults[key];
    const root = document.documentElement;

    switch(key) {
      case 'primaryColor':
        root.style.setProperty('--message-box', actualValue);
        break;
      case 'use_local':
        pywebview.api.use_local = actualValue;
        break;
    }
  },

  saveStorage() {
    pywebview.api.log(`Saving ${this.current.toString()}`, 10);
    console.log(this.current);
    localStorage.setItem('appSettings', JSON.stringify(this.current));

    console.log(localStorage.getItem('appSettings'));
  },
  
  applyAll() {
    Object.keys(this.defaults).forEach(key => {
      this.apply(key, this.get(key));
    });
  },

  reset() {
    this.current = this.defaults;
    this.setValues();
  },

  setValues() {
    const settings = SETTINGS.querySelectorAll('[data-settings');

    settings.forEach(value => {

        if (value.type == 'checkbox') {
          console.log(value.checked);
          value.checked = Settings.get(value.dataset.settings);
          value.dispatchEvent(new Event('change', { bubbles: true }));
        }
        else value.value = Settings.get(value.dataset.settings);

    });
  }
};

function setSettings(){
    pywebview.api.model = Settings.get('model');
    pywebview.api.api_key = Settings.get('api_key');
    pywebview.api.use_local = Settings.get('use_local');
    pywebview.api.system_message = Settings.get('system-message');

    pywebview.api.setModel(Settings.get('model'), Settings.get('api_key'));

    Settings.setValues();
    
    document.getElementById('primary-color-picker').value = Settings.get('primaryColor');

    
}

function saveSettings(){

    const settings = SETTINGS.querySelectorAll('[data-settings');

    settings.forEach(value => {
        
        if (value.type == 'checkbox') {
          console.log(value.checked);
          Settings.set(value.dataset.settings, value.checked);
        }
        else Settings.set(value.dataset.settings, value.value); 
    });

    Settings.saveStorage();
}

function startClose(){
    pywebview.api.close_app();
}