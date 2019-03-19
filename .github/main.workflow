workflow "push event" {
  on = "push"
  resolves = ["Slack Notification"]
}

action "Slack Notification" {
  uses = "Ilshidur/action-slack@e820f544affdbb77c1dee6d3f752f7f2daf4a0b3"
  secrets = ["GITHUB_TOKEN"]
  args = "A new commit has been pushed."
}

workflow "comment.workflow" {
  resolves = ["GitHub Action for Slack"]
  on = "commit_comment"
}

action "GitHub Action for Slack" {
  uses = "Ilshidur/action-slack@e820f544affdbb77c1dee6d3f752f7f2daf4a0b3"
}
