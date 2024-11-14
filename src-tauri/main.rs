// src-tauri/src/main.rs
use tauri::{CustomMenuItem, SystemTray, SystemTrayMenu, SystemTrayMenuItem, Window};

fn main() {
    tauri::Builder::default()
        .system_tray(SystemTray::new().with_menu(
            SystemTrayMenu::new()
                .add_item(CustomMenuItem::new("quit".to_string(), "Quit"))
        ))
        .invoke_handler(tauri::generate_handler![some_command])
        .build()
        .run()
        .expect("error while running tauri application");
}

#[tauri::command]
fn some_command(data: String) {
    println!("Received data: {}", data);
}
