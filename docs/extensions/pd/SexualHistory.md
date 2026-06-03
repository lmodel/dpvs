---
search:
  boost: 10.0
---

# Class: SexualHistory 


_Information about sexual history_



<div data-search-exclude markdown="1">



URI: [pd:SexualHistory](https://w3id.org/lmodel/dpv/pd/SexualHistory)





```mermaid
 classDiagram
    class SexualHistory
    click SexualHistory href "../SexualHistory/"
      Sexual <|-- SexualHistory
        click Sexual href "../Sexual/"
      
      
```





## Inheritance
* [Sexual](Sexual.md) [ [External](External.md)]
    * **SexualHistory**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [pd:SexualHistory](https://w3id.org/lmodel/dpv/pd/SexualHistory) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [PdSubset](PdSubset.md)



## Aliases


* Sexual History




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/pd/owl#SexualHistory |
| dpv_extension_slug | pd |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/pd




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pd:SexualHistory |
| native | pd:SexualHistory |
| exact | dpv_pd:SexualHistory, dpv_pd_owl:SexualHistory |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: SexualHistory
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#SexualHistory
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about sexual history
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Sexual History
exact_mappings:
- dpv_pd:SexualHistory
- dpv_pd_owl:SexualHistory
is_a: Sexual
class_uri: pd:SexualHistory

```
</details>

### Induced

<details>
```yaml
name: SexualHistory
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#SexualHistory
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about sexual history
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Sexual History
exact_mappings:
- dpv_pd:SexualHistory
- dpv_pd_owl:SexualHistory
is_a: Sexual
class_uri: pd:SexualHistory

```
</details></div>