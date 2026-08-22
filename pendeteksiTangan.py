import cv2
import mediapipe as mp
from gtts import gTTS
import pygame
import threading
import time
import os
import warnings

warnings.filterwarnings("ignore")

mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands


#---Fungsi untuk memainkan suara (pakai pygame aga stabil) ---
def play_sound(text):
    filename = f"voice_{text.replace(' ', '_').lower()}.mp3"
    tts = gTTS(text=text, lang='id')
    tts.save(filename)

    pygame.mixer.init()
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()

    #tunggu sampai suara selesai
    while pygame.mixer.music.get_busy():
        time.sleep(0.1) 

        pygame.mixer.quit()
        os.remove(filename)


        #---Fungsi deteksi gestur sederhana ---
        def detect_gesture(hand_landmarks):
            thumb_tip = landmarks.landmark[4].y
            index_tip = landmarks.landmark[8].y
            middle_tip = landmarks.landmark[12].y
            ring_tip = landmarks.landmark[16].y
            pinky_tip = landmarks.landmark[20].y

            thumb_base = landmarks.landmark[2].y
            index_base = landmarks.landmark[5].y

            #gestur "perkenalkan" tangan tebuka
            if (thumb_tip < thumb_base and index_tip < index_base and 
                 middle_tip <index_base and ring_tip < index_base and pinky_tip < index_base):
                 return "Halo"

            #gesture "nama saya" jari telunjuk tengak
            if (index_tip < index_base and middle_tip > index_base and ring_tip > index_base and pinky_tip > index_base and
                ring_tip > index_base and pinky_tip > index_base):
                return "Nama Saya"

            #gesture"cont" tangan menegapal
            if (index_tip > index_base and middle_tip > index_base and
                ring_tip > index_base and ring_tip > index_base):
                return "contoh"

#gesture "terima kasih" tanda love
            if (index_tip < index_base and pinky_tip < index_base and
                middle_tip > index_base and ring_tip > index_base):
                return "Terima Kasih"

            return None


        #---program utama---
        cap = cv2.VideoCapture(0)

        last_gesture = None
        last_time = 0

        #warna teks untuk setiap gesture
        gesture_colors =  {
            "Halo": (0, 255, 0),      # Hijau
            "Nama Saya": (0, 0, 255), # Biru
            "contoh": (255, 0, 0),    # Merah
            "Terima Kasih": (255, 255, 0)  # Kuning
        }

        with mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7) as hands:
            while true:
                ret, farme = cap.read()
                if not ret:
                    continue

                farme = cv2.flip(farme, 1)
                farme_rgb = cv2.cvtColor(farme, cv2.COLOR_BGR2RGB)
                results = hands.process(rgb_frame)

gesture = None
if results.multi_hand_landmarks:
    for hand_landmarks in results.multi_hand_landmarks:
        mp_drawing.draw_landmasrks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
        gesture = detect_gesture(hand_landmarks)

        if gesture:
            text = gesture
            color = gesture_colors.get(gesture, (255, 255, 255))  # Default warna putih
            font = cv2.FONT_HERSHEY_SIMPLEX

            #posisi pojok kiri atas
            x, y = 50, 80

#bayangan hitam tipis agar tetap terlihat
cv2.putText(frame, text, (x + 2, y + 2), font, 1, (0, 0, 0), 3, cv2.LINE_AA)

#teks utama dengan warna sesuai gesture
cv2.putText(frame, text, (x, y), font, 1.2, color, 2, cv2.LINE_AA)

#mainkan suara jika gesture baru terdeteksi
if gesture != last_gesture and time.time() - last_time > 2:  
    threading.Thread(target=play_sound, args=(gesture,)).start()
    last_gesture = gesture
    last_time = time.time()

    cv2.imshow("Hand Gesture Recognition", frame)

    #tekan esc untuk keluar
if cv2.waitKey(1) & 0xFF == 27:
    break

cap.release()
cv2.destroyAllWindows()