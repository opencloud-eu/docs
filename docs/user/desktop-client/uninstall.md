---
sidebar_position: 9
id: uninstall
title: Uninstall the Desktop Client
---

# Removing the OpenCloud Desktop App

If you no longer need the **OpenCloud Desktop Client**, follow these steps to completely remove it from your system.

## 1. Remove the Desktop App
The process depends on your operating system:

- **Windows:** Uninstall the app through **Control Panel > Programs & Features**.  
- **Mac:** Move the app to the **Trash** and empty it.  
- **Linux:** Use your **package manager** or remove the **AppImage** file manually.

## 2. Remove the Configuration File (Optional)
Even after uninstalling, the configuration file remains. This allows you to reinstall later without re-entering your connection details.

To completely remove the configuration file, you need to manually delete it.  
The exact location depends on your operating system.

## 3. Remove OpenCloud from the Windows Navigation Sidebar (Optional)

If you still see the OpenCloud shortcut in **File Explorer’s navigation bar**, follow these steps:

### Remove the Sidebar Entry via Registry Editor

1. Press **Windows Key + R**, type `regedit`, and press **Enter**.  
2. Open the **Registry Editor** and search for "OpenCloud":  
   - Press **Ctrl + F** and type **"OpenCloud"**.  
   - Press **Enter** to search.  
   - Press **F3** to find the next result.  
3. Look for the entry **System.IsPinnedToNameSpaceTree**.  
4. Right-click on it, select **Modify**, and change the value from **1** to **0**.  
5. Repeat this step for both **x64** and **x32** system settings.

 **No restart needed** – Just close and reopen **File Explorer**, and the sidebar entry will be gone.
