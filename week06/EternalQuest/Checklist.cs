using System.ComponentModel;
using MakingGoals;

namespace MakingGoals
{
    public class ChecklistGoal : Goal
    {
        public override int RecordEvent()
        {
            // check if the eventsCompleted == gaolTarget and if so _isCompleted = true
            // return points to total, and return bonus if completed
            _eventsCompleted += 1;
            if (_eventsCompleted == _goalTarget)
            {
                return _points + _goalBonus;
            }
            return _points;
        }

        public override string GetStringRepresentation()
        {
            return $"{_shortName}, {_description} this activity earns you {_points} - you have completed {_eventsCompleted}/{_goalTarget} events";
        }
    }
}