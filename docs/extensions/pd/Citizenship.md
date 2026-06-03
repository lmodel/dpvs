---
search:
  boost: 10.0
---

# Class: Citizenship 


_Information about citizenship_



<div data-search-exclude markdown="1">



URI: [pd:Citizenship](https://w3id.org/lmodel/dpv/pd/Citizenship)





```mermaid
 classDiagram
    class Citizenship
    click Citizenship href "../Citizenship/"
      External <|-- Citizenship
        click External href "../External/"
      
      
```





## Inheritance
* [External](External.md)
    * **Citizenship**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [pd:Citizenship](https://w3id.org/lmodel/dpv/pd/Citizenship) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [PdSubset](PdSubset.md)



## Aliases


* Citizenship




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/pd/owl#Citizenship |
| dpv_extension_slug | pd |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/pd




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pd:Citizenship |
| native | pd:Citizenship |
| exact | dpv_pd:Citizenship, dpv_pd_owl:Citizenship |
| close | iso29100:PersonallyIdentifiableInformation |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Citizenship
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#Citizenship
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about citizenship
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Citizenship
exact_mappings:
- dpv_pd:Citizenship
- dpv_pd_owl:Citizenship
close_mappings:
- iso29100:PersonallyIdentifiableInformation
is_a: External
class_uri: pd:Citizenship

```
</details>

### Induced

<details>
```yaml
name: Citizenship
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#Citizenship
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about citizenship
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Citizenship
exact_mappings:
- dpv_pd:Citizenship
- dpv_pd_owl:Citizenship
close_mappings:
- iso29100:PersonallyIdentifiableInformation
is_a: External
class_uri: pd:Citizenship

```
</details></div>