/*
 * Copyright (c) Meta Platforms and its affiliates.
 * This source code is licensed under the MIT license found in the
 * LICENSE file in the root directory of this source tree.
 */

const API_URL = process.env.REACT_APP__API_URL || "";

const urls = {
  client: {
    home: "/",
    qualification: (id) => `/qualifications/${id}`,
    task: (id) => `/tasks/${id}`,
    taskStats: (id) => `/tasks/${id}/stats`,
    taskTimeline: (id) => `/tasks/${id}/timeline`,
    taskUnit: (id, unitId) => `/tasks/${id}/units/${unitId}`,
    taskUnits: (id) => `/tasks/${id}/units`,
    taskWorkerOpinions: (id) => `/tasks/${id}/worker-opinions`,
    tasks: "/tasks",
  },
  server: {
    grantedQualifications: API_URL + "/api/granted-qualifications",
    qualification: (id) => API_URL + `/api/qualifications/${id}`,
    qualificationDetails: (id) => API_URL + `/api/qualifications/${id}/details`,
    qualifications: API_URL + "/api/qualifications",
    qualificationWorkers: (id) => API_URL + `/api/qualifications/${id}/workers`,
    qualificationGrantWorker: (id, workerId) =>
      API_URL + `/api/qualifications/${id}/workers/${workerId}/grant`,
    qualificationRevokeWorker: (id, workerId) =>
      API_URL + `/api/qualifications/${id}/workers/${workerId}/revoke`,
    stats: API_URL + "/api/review-stats",
    task: (id) => API_URL + `/api/tasks/${id}`,
    taskExportResults: (id) => API_URL + `/api/tasks/${id}/export-results`,
    taskExportResultsJson: (id, nUnits) =>
      API_URL + `/api/tasks/${id}/${nUnits}/export-results.json`,
    taskStatsResults: (id) => API_URL + `/api/tasks/${id}/stats-results`,
    taskTimeline: (id) => API_URL + `/api/tasks/${id}/timeline`,
    taskWorkerOpinions: (id) => API_URL + `/api/tasks/${id}/worker-opinions`,
    tasks: API_URL + "/api/tasks",
    tasksWorkerUnitsIds: (id) => API_URL + `/api/tasks/${id}/worker-units-ids`,
    unitReviewHtml: (id) => API_URL + `/api/units/${id}/review.html`,
    units: API_URL + "/api/units",
    unitsApprove: API_URL + "/api/units/approve",
    unitsDetails: API_URL + "/api/units/details",
    unitsReject: API_URL + "/api/units/reject",
    unitsSoftReject: API_URL + "/api/units/soft-reject",
    unitsOutputsFile: (id, filename) =>
      API_URL + `/api/units/${id}/static/${filename}`,
    unitsOutputsFileByFieldname: (id, fieldname) =>
      API_URL + `/api/units/${id}/static/fieldname/${fieldname}`,
    workerGrant: (id) => API_URL + `/api/workers/${id}/qualifications/grant`,
    workerGrantedQualifications: (id) =>
      API_URL + `/api/workers/${id}/qualifications`,
    workersBlock: (id) => API_URL + `/api/workers/${id}/block`,
  },
};

export default urls;
