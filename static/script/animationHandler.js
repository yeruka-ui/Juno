import {animate} from "https://cdn.jsdelivr.net/npm/motion@11.11.13/+esm";

export function chatAnimation(element) {
    animate(element,
        {
            opacity: [0, 1],
            y: [15, 0],
            filter: ["blur(8px)", "blur(0px)"]
        },
        {
            duration: 0.2,
            ease: "cubic-bezier(0.22, 1, 0.36, 1)"
        }
    );
}
