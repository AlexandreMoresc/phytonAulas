// Learn more about Tauri commands at https://tauri.app/develop/calling-rust/
use std::process::Command;
#[tauri::command]
fn greet(name: &str) -> String {
    format!("Hello, {}!", name)
}

#[tauri::command]
fn buscar_cnpj(cnpj: String) -> Result<String, String> {
    // Executa: python src-phyton/controller/busca.py "04.266.331/0019-58"
    let output = Command::new("python")
        .arg("../../src-phyton/controller/busca.py")
        .arg(&cnpj)
        .output()
        .map_err(|e| e.to_string())?;

    if output.status.success() {
        // Retorna stdout (JSON do Python)
        Ok(String::from_utf8_lossy(&output.stdout).to_string())
    } else {
        let error = String::from_utf8_lossy(&output.stderr);
        Err(error.to_string())
    }
}

#[cfg_attr(mobile, tauri::mobile_entry_point)]
pub fn run() {
    tauri::Builder::default()
        .plugin(tauri_plugin_opener::init())
        .invoke_handler(tauri::generate_handler![buscar_cnpj])
        .run(tauri::generate_context!())
        .expect("error while running tauri application");
}
