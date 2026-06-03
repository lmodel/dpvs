---
search:
  boost: 10.0
---

# Class: PerformanceAtWork 


_Information about performance at work or within work environments_



<div data-search-exclude markdown="1">



URI: [pd:PerformanceAtWork](https://w3id.org/lmodel/dpv/pd/PerformanceAtWork)





```mermaid
 classDiagram
    class PerformanceAtWork
    click PerformanceAtWork href "../PerformanceAtWork/"
      Professional <|-- PerformanceAtWork
        click Professional href "../Professional/"
      Behavioural <|-- PerformanceAtWork
        click Behavioural href "../Behavioural/"
      
      
```





## Inheritance
* [External](External.md)
    * [Behavioural](Behavioural.md)
        * **PerformanceAtWork** [ [Professional](Professional.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [pd:PerformanceAtWork](https://w3id.org/lmodel/dpv/pd/PerformanceAtWork) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [PdSubset](PdSubset.md)



## Aliases


* Performance at Work




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/pd/owl#PerformanceAtWork |
| dpv_extension_slug | pd |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/pd




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pd:PerformanceAtWork |
| native | pd:PerformanceAtWork |
| exact | dpv_pd:PerformanceAtWork, dpv_pd_owl:PerformanceAtWork |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: PerformanceAtWork
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#PerformanceAtWork
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about performance at work or within work environments
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Performance at Work
exact_mappings:
- dpv_pd:PerformanceAtWork
- dpv_pd_owl:PerformanceAtWork
is_a: Behavioural
mixins:
- Professional
class_uri: pd:PerformanceAtWork

```
</details>

### Induced

<details>
```yaml
name: PerformanceAtWork
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#PerformanceAtWork
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about performance at work or within work environments
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Performance at Work
exact_mappings:
- dpv_pd:PerformanceAtWork
- dpv_pd_owl:PerformanceAtWork
is_a: Behavioural
mixins:
- Professional
class_uri: pd:PerformanceAtWork

```
</details></div>