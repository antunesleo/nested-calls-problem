package main

import (
    "fmt"
    "net/http"
    "time"
)

func otherHandler(w http.ResponseWriter, r *http.Request) {
    fmt.Println("Success") 
}

func delayHandler(w http.ResponseWriter, r *http.Request) {
    duration := 100 * time.Second
    time.Sleep(duration)
    fmt.Println("Sleep done")
}

func main() {
    http.HandleFunc("/delay", delayHandler)
    http.HandleFunc("/other", otherHandler)
    fmt.Println("Server is running on http://localhost:8000")
    http.ListenAndServe(":8000", nil)
}
