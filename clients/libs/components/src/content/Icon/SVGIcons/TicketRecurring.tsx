import React from 'react';

const Icon = ({ className }: any) => (
  <svg
    xmlns="http://www.w3.org/2000/svg"
    width="30"
    height="23"
    fill="none"
    className={className + ' fill'}
    viewBox="0 0 30 23"
  >
    <g fill="#000" clipPath="url(#clip0)">
      <path d="M11.77 9.711c-1.196-.533-1.398-.81-1.398-1.228 0-.384.264-.794 1.003-.794.776 0 1.265.3 1.474.429a.38.38 0 00.338.032.423.423 0 00.243-.257l.332-.945a.453.453 0 00-.174-.533 3.608 3.608 0 00-1.527-.531v-.982c0-.241-.183-.438-.407-.438h-.824c-.224 0-.406.197-.406.438v1.093c-1.24.354-2.008 1.369-2.008 2.66 0 .72.233 1.31.713 1.807.383.396.934.739 1.734 1.076 1.098.48 1.249.908 1.249 1.3 0 .577-.473.965-1.176.965a2.96 2.96 0 01-1.689-.542.38.38 0 00-.353-.052.42.42 0 00-.255.268l-.32.96a.46.46 0 00.147.504c.454.349 1.147.603 1.865.685v1.036c0 .241.182.437.406.437h.837c.225 0 .407-.196.407-.438v-1.136c1.277-.37 2.1-1.459 2.1-2.788 0-.738-.202-1.344-.618-1.853-.374-.457-.912-.83-1.693-1.173zM28.656 18.399c-.715 1.332-1.867 2.358-3.245 2.85h2.277c.53 0 1.018-.31 1.274-.81s.239-1.11-.044-1.594l-.262-.446z"></path>
      <path d="M21.7 21.249H1.757c-.53 0-1.018-.31-1.274-.81s-.24-1.111.044-1.594l.984-1.678a.067.067 0 000-.067L.277 14.995a2.08 2.08 0 010-2.075l1.234-2.104a.068.068 0 000-.067L.277 8.644a2.081 2.081 0 010-2.075l1.234-2.105a.067.067 0 000-.067L.527 2.718a1.672 1.672 0 01-.044-1.593c.256-.5.744-.81 1.273-.81h25.932c.53 0 1.018.31 1.274.81.255.5.239 1.11-.044 1.593l-.985 1.679a.066.066 0 000 .067l1.234 2.104c.37.63.37 1.445 0 2.075l-1.234 2.105a.067.067 0 000 .067l.53.902a6.124 6.124 0 00-1.988-2.002l1.217-2.076a.067.067 0 000-.067l-1.234-2.104a2.08 2.08 0 010-2.075l.702-1.198h-6.252v.063c0 .519-.39.94-.873.94-.482 0-.872-.421-.872-.94v-.063H2.284l.703 1.198c.37.63.37 1.445 0 2.075L1.753 7.573a.067.067 0 000 .067l1.234 2.105c.37.63.37 1.444 0 2.075l-1.234 2.104a.067.067 0 000 .067l1.234 2.105c.37.63.37 1.445 0 2.075l-.703 1.197h16.811A5.892 5.892 0 0021.7 21.25zM28.61 11.97c.407.73.68 1.555.786 2.437.11-.5.033-1.04-.229-1.488l-.556-.95z"></path>
      <path d="M27.168 9.678c-1.373-1.111-3.066-1.58-4.767-1.32l-.933.142 1.285-1.847-.953-.77-2.503 3.598 3.295 2.714.724-1.02-1.703-1.401.956-.146c2.86-.438 5.517 1.714 5.923 4.795.406 3.082-1.591 5.944-4.451 6.382-2.86.437-5.518-1.715-5.924-4.796l-.084-.635-1.178.18.083.635c.242 1.832 1.13 3.453 2.504 4.565 1.373 1.111 3.065 1.58 4.766 1.32 1.7-.26 3.205-1.217 4.237-2.696 1.032-1.48 1.467-3.303 1.226-5.135-.241-1.832-1.13-3.453-2.503-4.565z"></path>
      <path
        fillRule="evenodd"
        d="M21.765 5.617L23 6.615l-1.135 1.632.512-.078c1.747-.267 3.486.215 4.897 1.357 1.41 1.142 2.324 2.808 2.572 4.69.248 1.882-.2 3.757-1.26 5.276-1.06 1.52-2.606 2.504-4.353 2.771-1.747.267-3.487-.215-4.898-1.357-1.41-1.142-2.324-2.808-2.572-4.69l-.108-.824 1.529-.233.108.823c.392 2.978 2.96 5.056 5.724 4.634 2.764-.422 4.693-3.189 4.301-6.166-.392-2.977-2.96-5.056-5.724-4.634l-.537.082 1.507 1.242-.938 1.321-3.574-2.944 2.714-3.9zm.07.533l-2.291 3.294 3.015 2.484.51-.717L21.17 9.65l1.373-.21c2.957-.452 5.703 1.772 6.123 4.957.42 3.186-1.645 6.145-4.602 6.597-2.957.452-5.703-1.772-6.123-4.957l-.058-.447-.83.127.06.446c.234 1.782 1.098 3.358 2.434 4.44 1.335 1.081 2.98 1.537 4.635 1.284 1.654-.253 3.117-1.184 4.12-2.623 1.004-1.438 1.428-3.211 1.193-4.993-.235-1.782-1.099-3.358-2.435-4.44-1.335-1.08-2.98-1.537-4.635-1.284l-1.355.207 1.435-2.062-.67-.54z"
        clipRule="evenodd"
      ></path>
    </g>
    <defs>
      <clipPath id="clip0">
        <path fill="#fff" d="M0 0H30V22.5H0z"></path>
      </clipPath>
    </defs>
  </svg>
);

Icon.displayName = 'Icon.TicketRecurring';

export default Icon;
