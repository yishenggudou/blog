workflow "push event" {
  on = "push"
  resolves = ["Slack Notification"]
}

action "Slack Notification" {
  uses = "rtCamp/action-slack-notify@v1.0.0"
  secrets = ["GITHUB_TOKEN"]
}

workflow "comment.workflow" {
  resolves = ["GitHub Action for Slack"]
  on = "commit_comment"
}

action "GitHub Action for Slack" {
  uses = "Ilshidur/action-slack@e820f544affdbb77c1dee6d3f752f7f2daf4a0b3"
}
