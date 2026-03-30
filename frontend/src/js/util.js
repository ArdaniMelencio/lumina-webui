// Textarea utility functions
function resize_input() {
    // Reset and expand textarea height based on content
    INPUT_TEXT.style.height = '30px';
    INPUT_TEXT.style.height = `${INPUT_TEXT.scrollHeight + 2}px`;
}

function scroll_down() {
    // Scroll chat container to bottom to show latest messages
    CHATBOX.scrollTop = CHATBOX.scrollHeight;
}

// Settings panel navigation
function changeSettingsDisplay(button) {
    const panelName = button.dataset.panel;
    const templateId = `${panelName}-panel`;
    const template = document.getElementById(templateId);
    const display = document.getElementById('settings-display');
    const panels = display.querySelectorAll('[class="display"]');
    
    // Hide all panels, then show the selected one
    panels.forEach(panel => panel.style.display = 'none');
    template.style.display = 'block';
}

// Settings management object
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
      // Try localStorage first, if none, create new settings
      localStorage.getItem('appSettings');
      return localStorage;
    } catch (e) {
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
    return this.current[key] ?? this.defaults[key]; // Auto-fallback to defaults
  },
  
  set(key, value) {
    this.current[key] = value;
    localStorage.setItem('appSettings', JSON.stringify(this.current));
    this.apply(key, value);
  },
  
  apply(key, value) {
    const actualValue = value ?? this.defaults[key];
    const root = document.documentElement
    
    switch(key) {
      case 'primaryColor':
        root.style.setProperty('--message-box', actualValue);
        break;
      // Add more CSS variable mappings as needed
      case 'use_local':
        pywebview.api.use_local = actualValue;
        break;
    }
  },

  saveStorage() {
    try {
      pywebview.api.log(`Saving settings: ${JSON.stringify(this.current)}`, 10);
      localStorage.setItem('appSettings', JSON.stringify(this.current));
      pywebview.api.log("Settings saved successfully", 10);
    } catch (e) {
      pywebview.api.log("Failed to save settings to storage", 40);
    }
  },
  
  applyAll() {
    // Apply all current settings to the UI
    Object.keys(this.defaults).forEach(key => {
        this.apply(key, this.get(key));
    });
    pywebview.api.log("All settings applied to UI", 10);
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
  try {
    // Send all settings as a single object
    const settingsData = {
      model: Settings.get('model'),
      api_key: Settings.get('api_key'), 
      use_local: Settings.get('use_local'),
      system_message: Settings.get('system-message')
    };
        
    pywebview.api.update_settings(settingsData);
    pywebview.api.log("All settings synchronized with backend", 10);
      
    // Populate settings form fields with current values
    const settings = SETTINGS.querySelectorAll('[data-settings]');
    settings.forEach(value => {
      value.value = Settings.get(value.dataset.settings);
    });
        
    document.getElementById('primary-color-picker').value = Settings.get('primaryColor');
    Settings.setValues();
    pywebview.api.log("Settings form populated", 10);
    
    } catch (e) {
        pywebview.api.log("Error syncing settings with backend", 40);
    }
}

function saveSettings() {
    try {
        // Save all settings from form fields to storage
        const settings = SETTINGS.querySelectorAll('[data-settings]');
        settings.forEach(value => {
            
        if (value.type == 'checkbox') {
          console.log(value.checked);
          Settings.set(value.dataset.settings, value.checked);
        }
        else Settings.set(value.dataset.settings, value.value); 
        });
        Settings.saveStorage();
        pywebview.api.log("All settings saved from form", 10);
    } catch (e) {
        pywebview.api.log("Failed to save settings from form", 40);
    }
}

function startClose() {
    try {
        // Save settings and close application
        saveSettings();
        pywebview.api.log("Application closing initiated", 10);
        pywebview.api.close_app();
    } catch (e) {
        pywebview.api.log("Error during application close", 50);
    }
}