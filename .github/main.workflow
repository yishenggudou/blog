workflow "push event" {
  on = "push"
  resolves = ["Slack Notification"]
}

action "Slack Notification" {
  uses = "rtCamp/action-slack-notify@v1.0.0"
  secrets = ["GITHUB_TOKEN"]
}
