---
search:
  boost: 10.0
---

# Class: DNACode 


_Information about DNA_



<div data-search-exclude markdown="1">



URI: [pd:DNACode](https://w3id.org/lmodel/dpv/pd/DNACode)





```mermaid
 classDiagram
    class DNACode
    click DNACode href "../DNACode/"
      MedicalHealth <|-- DNACode
        click MedicalHealth href "../MedicalHealth/"
      
      
```





## Inheritance
* [MedicalHealth](MedicalHealth.md) [ [External](External.md)]
    * **DNACode**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [pd:DNACode](https://w3id.org/lmodel/dpv/pd/DNACode) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [PdSubset](PdSubset.md)



## Aliases


* DNA Code




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/pd/owl#DNACode |
| dpv_extension_slug | pd |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/pd




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pd:DNACode |
| native | pd:DNACode |
| exact | dpv_pd:DNACode, dpv_pd_owl:DNACode |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: DNACode
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#DNACode
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about DNA
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- DNA Code
exact_mappings:
- dpv_pd:DNACode
- dpv_pd_owl:DNACode
is_a: MedicalHealth
class_uri: pd:DNACode

```
</details>

### Induced

<details>
```yaml
name: DNACode
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#DNACode
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about DNA
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- DNA Code
exact_mappings:
- dpv_pd:DNACode
- dpv_pd_owl:DNACode
is_a: MedicalHealth
class_uri: pd:DNACode

```
</details></div>