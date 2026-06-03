---
search:
  boost: 10.0
---

# Class: Job 


_Information about professional jobs_



<div data-search-exclude markdown="1">



URI: [pd:Job](https://w3id.org/lmodel/dpv/pd/Job)





```mermaid
 classDiagram
    class Job
    click Job href "../Job/"
      Professional <|-- Job
        click Professional href "../Professional/"
      
      
```





## Inheritance
* [Social](Social.md)
    * [Professional](Professional.md)
        * **Job**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [pd:Job](https://w3id.org/lmodel/dpv/pd/Job) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [PdSubset](PdSubset.md)



## Aliases


* Job




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/pd/owl#Job |
| dpv_extension_slug | pd |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/pd




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pd:Job |
| native | pd:Job |
| exact | dpv_pd:Job, dpv_pd_owl:Job |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Job
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#Job
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about professional jobs
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Job
exact_mappings:
- dpv_pd:Job
- dpv_pd_owl:Job
is_a: Professional
class_uri: pd:Job

```
</details>

### Induced

<details>
```yaml
name: Job
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#Job
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about professional jobs
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Job
exact_mappings:
- dpv_pd:Job
- dpv_pd_owl:Job
is_a: Professional
class_uri: pd:Job

```
</details></div>