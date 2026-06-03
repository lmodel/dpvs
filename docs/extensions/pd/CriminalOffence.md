---
search:
  boost: 10.0
---

# Class: CriminalOffence 


_Information about criminal offences_



<div data-search-exclude markdown="1">



URI: [pd:CriminalOffence](https://w3id.org/lmodel/dpv/pd/CriminalOffence)





```mermaid
 classDiagram
    class CriminalOffence
    click CriminalOffence href "../CriminalOffence/"
      Criminal <|-- CriminalOffence
        click Criminal href "../Criminal/"
      
      
```





## Inheritance
* [Social](Social.md)
    * [Criminal](Criminal.md)
        * **CriminalOffence**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [pd:CriminalOffence](https://w3id.org/lmodel/dpv/pd/CriminalOffence) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [PdSubset](PdSubset.md)



## Aliases


* Criminal Offence




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/pd/owl#CriminalOffence |
| dpv_extension_slug | pd |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/pd




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pd:CriminalOffence |
| native | pd:CriminalOffence |
| exact | dpv_pd:CriminalOffence, dpv_pd_owl:CriminalOffence |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: CriminalOffence
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#CriminalOffence
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about criminal offences
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Criminal Offence
exact_mappings:
- dpv_pd:CriminalOffence
- dpv_pd_owl:CriminalOffence
is_a: Criminal
class_uri: pd:CriminalOffence

```
</details>

### Induced

<details>
```yaml
name: CriminalOffence
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#CriminalOffence
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about criminal offences
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Criminal Offence
exact_mappings:
- dpv_pd:CriminalOffence
- dpv_pd_owl:CriminalOffence
is_a: Criminal
class_uri: pd:CriminalOffence

```
</details></div>