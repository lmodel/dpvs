---
search:
  boost: 10.0
---

# Class: LifeHistory 


_Information about personal history regarding events or activities -_

_including their occurrences that might be directly related or have had_

_an influence (e.g. World War, 9/11)_



<div data-search-exclude markdown="1">



URI: [pd:LifeHistory](https://w3id.org/lmodel/dpv/pd/LifeHistory)





```mermaid
 classDiagram
    class LifeHistory
    click LifeHistory href "../LifeHistory/"
      Historical <|-- LifeHistory
        click Historical href "../Historical/"
      
      
```





## Inheritance
* [Historical](Historical.md)
    * **LifeHistory**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [pd:LifeHistory](https://w3id.org/lmodel/dpv/pd/LifeHistory) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [PdSubset](PdSubset.md)



## Aliases


* Life History




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/pd/owl#LifeHistory |
| dpv_extension_slug | pd |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/pd




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pd:LifeHistory |
| native | pd:LifeHistory |
| exact | dpv_pd:LifeHistory, dpv_pd_owl:LifeHistory |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: LifeHistory
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#LifeHistory
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: 'Information about personal history regarding events or activities -

  including their occurrences that might be directly related or have had

  an influence (e.g. World War, 9/11)'
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Life History
exact_mappings:
- dpv_pd:LifeHistory
- dpv_pd_owl:LifeHistory
is_a: Historical
class_uri: pd:LifeHistory

```
</details>

### Induced

<details>
```yaml
name: LifeHistory
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#LifeHistory
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: 'Information about personal history regarding events or activities -

  including their occurrences that might be directly related or have had

  an influence (e.g. World War, 9/11)'
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Life History
exact_mappings:
- dpv_pd:LifeHistory
- dpv_pd_owl:LifeHistory
is_a: Historical
class_uri: pd:LifeHistory

```
</details></div>