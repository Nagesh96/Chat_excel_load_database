
import logging

class ExpAG:
    def __init__(self,batch_id,params):
        self.params = params
        self.batch_id = batch_id
        self.error_status = False
        logging.getlogger().setLevel(logging.INFO)
        self.insert_ag = """
    BEGIN
        -- SET NOCOUNT ON added to prevent extra result sets from
        -- interfering with SELECT statements
        SET NOCOUNT ON;
        SET XACT_ABORT ON;
            BEGIN TRANSACTION

                insert into daedbo.dae_tabi_expag
            (
            
        [t_expag_tskid],
        [s_expag_datetime_received],
        [s_expag_starttime],
        [s_expag_endtime],
        [t_expag_dept_desc],
        [t_expag_task-desc],
        [t_expag_action_desc],
        [t_expag_status_desc],
        [t_expag_oper_name],
        [t_expag_pi_date],
        [t_expag_lan_id],
        [s_expag_inserttimestamp]
            )

            select
            [tskid],
            cast(datercvd as datetime) + cast(timercvd as datetime),
            cast([pidate] as datetime) + cast(starttime as datetime),
            case
            when cast([pidate] as datetime) + cast(endtime as datetime) < cast([pidate] as datetime) + cast(starttime as datetime)
            then dateadd(day,1, cast([pidate] as datetime) + cast(endtime as datetime))
            else cast([pidate] as datetime) + cast(endtime as datetime)
        end,
            [dtpdesc],
            [tskdesc],
            [actdesc],
            [startusdesc],
            [opername],
            [pidate],
            upper([operid]),
            CURRENT_TIMESTAMP

            FROM #ag_file
            where CONCAT(CONVERT(varchar,[tskid]), CONVERT(varchar, convert(time, [starttime])),CONVERT(varchar, convert(time, [endtime])),convert(varchar,[dptdesc])) not in
            (select CONCAT(CONVERT(varchar,t_expag_tskid),CONVERT(varchar, convert(time, s_expag_starttime)),CONVERT(varchar,convert(time, s_expag_endtime)),CONVERT(varchar,t_expag_dept_desc))
            from [daedbo].[dae_tabi_expag])
            COMMIT TRANSACTION
        END
"""
