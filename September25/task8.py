result = match value:
    case 0 => "zero"
    case x if x > 0 => "positive"
    case x if x < 0 => "negative"
    case _ => "other"
