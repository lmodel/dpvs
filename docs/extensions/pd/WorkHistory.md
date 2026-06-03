---
search:
  boost: 10.0
---

# Class: WorkHistory 


_Information about work history in a professional context_



<div data-search-exclude markdown="1">



URI: [pd:WorkHistory](https://w3id.org/lmodel/dpv/pd/WorkHistory)





```mermaid
 classDiagram
    class WorkHistory
    click WorkHistory href "../WorkHistory/"
      Professional <|-- WorkHistory
        click Professional href "../Professional/"
      
      
```





## Inheritance
* [Social](Social.md)
    * [Professional](Professional.md)
        * **WorkHistory**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [pd:WorkHistory](https://w3id.org/lmodel/dpv/pd/WorkHistory) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [PdSubset](PdSubset.md)



## Aliases


* Work History




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/pd/owl#WorkHistory |
| dpv_extension_slug | pd |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/pd




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pd:WorkHistory |
| native | pd:WorkHistory |
| exact | dpv_pd:WorkHistory, dpv_pd_owl:WorkHistory |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: WorkHistory
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#WorkHistory
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about work history in a professional context
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Work History
exact_mappings:
- dpv_pd:WorkHistory
- dpv_pd_owl:WorkHistory
is_a: Professional
class_uri: pd:WorkHistory

```
</details>

### Induced

<details>
```yaml
name: WorkHistory
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#WorkHistory
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about work history in a professional context
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Work History
exact_mappings:
- dpv_pd:WorkHistory
- dpv_pd_owl:WorkHistory
is_a: Professional
class_uri: pd:WorkHistory

```
</details></div>