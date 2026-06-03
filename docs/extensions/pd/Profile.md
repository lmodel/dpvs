---
search:
  boost: 10.0
---

# Class: Profile 


_Profile or user profile is information and representation of_

_characteristics associated with person(s) or group(s)_



<div data-search-exclude markdown="1">



URI: [pd:Profile](https://w3id.org/lmodel/dpv/pd/Profile)





```mermaid
 classDiagram
    class Profile
    click Profile href "../Profile/"
      Profile <|-- GroupProfile
        click GroupProfile href "../GroupProfile/"
      Profile <|-- IndividualProfile
        click IndividualProfile href "../IndividualProfile/"
      
      
```





## Inheritance
* **Profile**
    * [GroupProfile](GroupProfile.md)
    * [IndividualProfile](IndividualProfile.md)


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [pd:Profile](https://w3id.org/lmodel/dpv/pd/Profile) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [PdSubset](PdSubset.md)



## Aliases


* Profile




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/pd/owl#Profile |
| dpv_extension_slug | pd |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/pd




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pd:Profile |
| native | pd:Profile |
| exact | dpv_pd:Profile, dpv_pd_owl:Profile |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Profile
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#Profile
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: 'Profile or user profile is information and representation of

  characteristics associated with person(s) or group(s)'
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Profile
exact_mappings:
- dpv_pd:Profile
- dpv_pd_owl:Profile
class_uri: pd:Profile

```
</details>

### Induced

<details>
```yaml
name: Profile
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#Profile
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: 'Profile or user profile is information and representation of

  characteristics associated with person(s) or group(s)'
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Profile
exact_mappings:
- dpv_pd:Profile
- dpv_pd_owl:Profile
class_uri: pd:Profile

```
</details></div>