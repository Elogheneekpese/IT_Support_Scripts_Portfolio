# Printer Troubleshooting Guide

**What Is This?**  
This guide provides step-by-step instructions to diagnose and fix common printer issues faced by users in a workplace or home office setting. It’s designed for both end-users and IT Support staff to quickly restore printing functionality without waiting for escalation.

---

## 1. Printer Is Offline or Not Responding

This is a common issue where the printer shows as "offline" or doesn't respond when you try to print.

### Fix Steps:
- **Check power:** Ensure the printer is plugged in and powered on.
- **Check display:** Look for any error codes or paper jams on the printer screen.
- **USB or network cable:** Reconnect cables or verify the printer is connected to Wi-Fi.
- **Restart the printer.** Unplug for 10 seconds, then power it back on.
- **Restart the computer.**

---

## 2. Printer Queue Stuck / Print Jobs Not Processing

Sometimes documents get "stuck" in the print queue, especially after an error.

### Fix Steps:
- Open **Control Panel > Devices and Printers**
- Right-click on the printer > **See what’s printing**
- Click **Printer** menu > Uncheck **Use Printer Offline**
- Cancel all documents in the queue
- Restart the **Print Spooler**:
  1. Open **Command Prompt as Administrator**
  2. Run:
     ```
     net stop spooler
     net start spooler
     ```

---

## 3. Wireless Printer Connection Issues

For Wi-Fi printers that are not detected or dropping connection:

### Fix Steps:
- **Verify printer is connected to the correct Wi-Fi network**
- Print a **network status page** from the printer's menu to confirm IP address
- On the PC, **remove the printer** from settings, then **re-add** it
- Restart router and printer
- If your network uses guest mode, make sure the printer is not isolated from the PC

---

## 4. Set the Correct Printer as Default

Windows sometimes defaults to the wrong printer (like "OneNote" or "PDF").

### Fix Steps:
- Go to **Settings > Devices > Printers & Scanners**
- Click your preferred printer > **Set as default**
- Uncheck **"Let Windows manage my default printer"** (if enabled)

---

## 5. Install or Update Printer Drivers

Outdated or incorrect drivers often cause printing failures or missing options.

### Fix Steps:
- Visit the manufacturer’s official website (e.g., HP, Canon, Epson)
- Download the **latest driver** for your model and Windows version
- Uninstall old drivers if necessary:
  - Control Panel > Programs > Uninstall a program
- Reinstall the driver and reboot your PC

---

## 6. Cannot Print from Specific App (e.g., Excel, Outlook)

If printing works from Notepad but fails from Office apps:

### Fix Steps:
- Try printing another document from the same app
- Repair the app (e.g., Microsoft Office) via:
  - **Settings > Apps > Installed Apps > Modify > Repair**
- Check if the app has a custom print setting that needs to be reset

---

## 7. Low Ink / Toner or Paper Jam

Hardware-level issues can also stop print jobs or create errors.

### Fix Steps:
- Open printer panel and check for:
  - Jammed paper
  - Low ink or toner warning
  - Misaligned trays or cartridges
- Clean rollers and sensors (if trained to do so)

---

## 8. General Maintenance Tips

- Turn printer off when not in use for long periods
- Keep firmware updated
- Use quality paper to avoid jams
- Regularly check and clean internal components if trained or as per user manual

---

## Printer Troubleshooting Checklist

| Step                                      | Tried? |
|-------------------------------------------|--------|
| Checked power and cable connections       | ⬜️      |
| Restarted printer and computer            | ⬜️      |
| Cleared print queue                       | ⬜️      |
| Restarted Print Spooler service           | ⬜️      |
| Verified Wi-Fi or Ethernet connectivity   | ⬜️      |
| Set correct printer as default            | ⬜️      |
| Installed or updated printer drivers      | ⬜️      |
| Checked paper jams or low ink/toner       | ⬜️      |
| Repaired printing software (Office, etc.) | ⬜️      |

---

*End of guide.*
